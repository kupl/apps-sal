class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = threshold * k
        s1 = sum(arr[:k])
        n = len(arr)
        c = 0
        if s1 >= s:
            c += 1
        for i in range(k, n):
            s1 -= arr[i - k]
            s1 += arr[i]
            if s1 >= s:
                c += 1
        return c
