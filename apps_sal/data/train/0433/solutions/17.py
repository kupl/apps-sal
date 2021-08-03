class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        a = 0
        f = 0
        for i in range(len(arr)):
            a = a + 1
            c = c + arr[i]
            while a >= k:
                if c / k >= threshold:
                    f = f + 1
                c = c - arr[i - a + 1]
                a = a - 1
        return f
