class Solution:
    def atMostK(self, arr, k):
        d = {}
        l, r = 0, 0
        count = 0
        while r < len(arr):
            if arr[r] not in d:
                d[arr[r]] = 0
            d[arr[r]] += 1

            while len(d) > k:
                d[arr[l]] -= 1
                if d[arr[l]] == 0:
                    d.pop(arr[l])
                l += 1

            count += r - l + 1
            r += 1
        return count
    
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A,K-1)
