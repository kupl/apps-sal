# [google ][Jenny_write 20201003 1:32 am ]

# [Jenny_write]1016. Binary String With Substrings Representing 1 To N 
# [Jenny_write]114. Longest Common Prefix
# [Jenny_write]len(A) - len(set(A)) >= 1 


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        sources_dict = {}
        targets_dict ={}

        for i, pos_index in enumerate(indexes):
            sources_dict[pos_index] = sources[i]
            targets_dict[pos_index] = targets[i]

        # 此处一定要先建字典，再倒排序
        indexes.sort(reverse=True)

        for pos_index in indexes:
            source = sources_dict[pos_index]
            target = targets_dict[pos_index]
            tmp_str = S[pos_index:(pos_index + len(source))]
            if tmp_str == source:
                S = S[:pos_index] +target +S[pos_index+len(source):]
        return (S)


