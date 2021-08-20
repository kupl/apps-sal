class Solution:

    def numOfSubarrays(self, A):
        ans = even = odd = 0
        for x in A:
            if x % 2:
                (odd, even) = (1 + even, odd)
            else:
                even += 1
            ans += odd
        return ans % (10 ** 9 + 7)
