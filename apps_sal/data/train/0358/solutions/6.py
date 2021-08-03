class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        index_position = dict()
        r_list = []

        for pos, index in enumerate(indexes):
            source_len = len(sources[pos])
            if S[index:index + source_len] == sources[pos]:
                index_position[index] = pos

        next_index = 0
        for i in range(len(S)):
            if i < next_index:
                continue
            if i in index_position:
                pos = index_position[i]
                r_list.append(targets[pos])
                next_index += len(sources[pos])
            else:
                r_list.append(S[i])
                next_index += 1

        return ''.join(r_list)
