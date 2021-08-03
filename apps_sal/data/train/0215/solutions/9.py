def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if(nums == [1]):
            return True
        i = 0
        a = nums[i]
        for j in range(i + 1, len(nums)):
            if(a < nums[j]):
                b = gcd(nums[j], a)
                if(b == 1):
                    return True
                else:
                    a = b
            else:
                b = (gcd(a, nums[j]))
                if(b == 1):
                    return True
                else:
                    a = b
        return False
