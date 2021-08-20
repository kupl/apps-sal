class Solution:

    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        mx = -float('inf')
        mn = float('inf')
        n = 0
        for i in arr:
            mx = max(mx, i)
            mn = min(mn, i)
            n += 1
        d = dict()
        for i in range(mn, mx + 1):
            d[i] = 0
        if diff > 0:
            d[arr[0]] = 1
            for i in range(1, n):
                if arr[i] - diff >= mn:
                    d[arr[i]] = max(d[arr[i]], d[arr[i] - diff] + 1)
                else:
                    d[arr[i]] = 1
        else:
            arr = arr[::-1]
            d[arr[0]] = 1
            for i in range(1, n):
                if arr[i] + diff >= mn:
                    d[arr[i]] = max(d[arr[i]], d[arr[i] + diff] + 1)
                else:
                    d[arr[i]] = 1
        return max(list(d.values()))
