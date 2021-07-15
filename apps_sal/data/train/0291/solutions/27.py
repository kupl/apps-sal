class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even = 0, 1
        s = res = 0
        for n in arr:
            s += n

            if s % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1

            res %= 1000000007

        return res
