

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:

        s_dict = {}
        t_dict = {}
        for i, index in enumerate(indexes):
            s_dict[index] = sources[i]
            t_dict[index] = targets[i]

        indexes.sort(reverse=True)

        for index in indexes:
            sour = s_dict[index]
            targ = t_dict[index]
            le_s = len(sour)
            tmp_str = S[index:(index + le_s)]

            if tmp_str == sour:
                S = S[:index] + targ + S[index + le_s:]
        return S
