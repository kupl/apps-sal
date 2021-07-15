class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic = collections.Counter(s)
        for letter in t:
            if letter in dic and dic[letter] > 0:
                dic[letter] -= 1
        return sum(dic.values())
