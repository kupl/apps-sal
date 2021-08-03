class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        dic = collections.defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(i + minSize - 1, min(i + maxSize, n)):
                temp = s[i:j + 1]
                if len(set(temp)) <= maxLetters:
                    dic[temp] += 1
                    res = max(res, dic[temp])
        return res
