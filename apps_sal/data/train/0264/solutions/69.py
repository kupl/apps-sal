class Solution:

    def maxLength(self, arr: List[str]) -> int:
        arr = [w for w in arr if len(w) == len(set(w))]
        hm = {}
        res = 0
        dp = {0: 0}
        for (i, w) in enumerate(arr):
            bitmask = 0
            for c in set(w):
                bit_set = 1 << ord(c) - ord('a')
                bitmask ^= bit_set
            hm[i] = bitmask
        for i in range(len(arr)):
            for p in list(dp.keys()):
                if not hm[i] & p:
                    now = hm[i] ^ p
                    dp[now] = max(dp.get(now, 0), dp[p] + len(arr[i]))
        return max(dp.values())
