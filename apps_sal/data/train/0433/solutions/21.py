class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        rep = 0
        target = k * threshold

        cur = sum(arr[:k])
        if cur >= target:
            rep += 1
        l, r = 0, k
        while r < len(arr):
            cur -= arr[l]
            cur += arr[r]
            l += 1
            r += 1
            if cur >= target:
                rep += 1
        return rep
