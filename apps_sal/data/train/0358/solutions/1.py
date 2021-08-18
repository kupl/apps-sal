

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        sources_dict = {}
        targets_dict = {}

        for i, pos_index in enumerate(indexes):
            sources_dict[pos_index] = sources[i]
            targets_dict[pos_index] = targets[i]

        indexes.sort(reverse=True)

        for pos_index in indexes:
            source = sources_dict[pos_index]
            target = targets_dict[pos_index]
            tmp_str = S[pos_index:(pos_index + len(source))]
            if tmp_str == source:
                S = S[:pos_index] + target + S[pos_index + len(source):]
        return (S)
