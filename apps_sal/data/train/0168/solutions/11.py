class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dict = {}
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        num_of_distinct = 0
        for key in dict.keys():
            if dict[key] % 2 == 1:
                num_of_distinct += 1
        return num_of_distinct <= k and k <= len(s)
