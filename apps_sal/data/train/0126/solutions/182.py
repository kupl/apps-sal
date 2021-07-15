import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = collections.defaultdict(int)
        for i in range(len(s) - minSize + 1):
            if len(collections.Counter(s[i:i + minSize])) <= maxLetters:
                dic[s[i:i + minSize]] += 1
        if not dic:
            return 0
        return max(dic.values())

