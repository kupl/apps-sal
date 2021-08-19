class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_dict = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        integrals = [(False, False, False, False, False)]
        for l in s:
            vector = list(integrals[-1])
            if l in vowel_dict:
                vector[vowel_dict[l]] = not vector[vowel_dict[l]]
            integrals.append(tuple(vector))
        seen = {}
        res = 0
        for i, v in enumerate(integrals):
            if v in seen:
                res = max(res, i - seen[v])
            else:
                seen[v] = i
        return res
#         start, end = 0, 0

#         for i in range(0, len(s)-1):
#             if s[i] in vowel_dict:
#                 vowel_dict[s[i]] +=1
#                 end +=1

#             end += 1
