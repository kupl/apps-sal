class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        cache = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, k, res = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in cache:
                k ^= cache[c]
            # 如果k之前出现过，那么说明这中间这段是满足条件的
            if k not in d:
                d[k] = i
            else:
                res = max(res, i - d[k])
        return res
