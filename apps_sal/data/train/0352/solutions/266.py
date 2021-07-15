from collections import Counter
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        def helper(s1, s2):
            if len(s1) != len(s2) - 1:
                return False
            s1 = Counter(s1)
            s2 = Counter(s2)
            diff = 0
            for j in s2:
                if j not in s1:
                    diff += 1
                elif s2[j] != s1[j]:
                    diff += 1
                if diff >= 2:
                    return False
            return diff == 1
    
        dps = [1 for _ in words]
        for j in range(len(words)):
            _max = 1
            for i in range(j):
                if helper(words[i], words[j]):
                    _max = max(_max, dps[i] + 1)
            dps[j] = _max
        return max(dps)
            

