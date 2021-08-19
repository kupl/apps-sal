class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        even = 0
        odd = 0
        c = 0
        for e in arr:
            if e % 2 == 1:
                c += 1 + even
                (even, odd) = (odd, even + 1)
            else:
                c += odd
                even += 1
        return c % (10 ** 9 + 7)
