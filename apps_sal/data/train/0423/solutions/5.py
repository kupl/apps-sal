class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        mx = max(arr)
        mn = min(arr)
        d = dict()
        for i in range(-10**4, 10**4 + 1):
            d[i] = 0
        n = len(arr)
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
