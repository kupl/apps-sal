class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = {}
        for i in range(len(s)-minSize+1):
            s1 = s[i:i+minSize]
            unique = {}
            for c in s1:
                if c not in unique:
                    unique[c] = 1
            if len(unique) <= maxLetters:
                if s1 in dic:
                    dic[s1] += 1
                else:
                    dic[s1] = 1
                if i != len(s)-minSize and minSize != maxSize:
                    s2 = s[i:i+maxSize]
                    if s2[-1] not in unique:
                        unique[s2[-1]] = 1
                    if len(unique) <= maxLetters:
                        if s2 in dic:
                            dic[s2] += 1
                        else:
                            dic[s2] = 1
        max_occr = 0
        for key in dic:
            if dic[key] > max_occr:
                max_occr = dic[key]
        return max_occr
