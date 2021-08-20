class Solution:

    def minSteps(self, s: str, t: str) -> int:
        dict1 = {}
        dict2 = {}
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in t:
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1
        c_chars = 0
        d_chars = 0
        for i in dict1:
            if i in dict2:
                if dict2[i] > dict1[i]:
                    c = dict2[i] - dict1[i]
                else:
                    c = dict1[i] - dict2[i]
                c_chars += c
            else:
                d_chars += dict1[i]
        for i in dict2:
            if i not in dict1:
                d_chars += dict2[i]
        return (c_chars + d_chars) // 2
