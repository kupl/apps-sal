# [google ][Jenny_write 20201003 1:32 am ]

# [Jenny_write]1016. Binary String With Substrings Representing 1 To N
# [Jenny_write]14. Longest Common Prefix
# [Jenny_write]

# 20201003 3:31 pm -3:39 pm

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:

        # Step 1: dict
        s_dict = {}
        t_dict = {}
        for i, index in enumerate(indexes):
            s_dict[index] = sources[i]
            t_dict[index] = targets[i]

        # Step 2 : revs_sort
        indexes.sort(reverse=True)

        # Step 3 : if

        for index in indexes:
            sour = s_dict[index]
            targ = t_dict[index]
            le_s = len(sour)
            tmp_str = S[index:(index + le_s)]

            if tmp_str == sour:
                # if true, replce
                S = S[:index] + targ + S[index + le_s:]
        return S
