class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 1
        res = 0
        sum = 0
        for i in arr:
            sum += i
            if sum % 2 == 0:
                even += 1
                res = (res + odd) % 1000000007
            else:
                odd += 1
                res = (res + even) % 1000000007
        return res
