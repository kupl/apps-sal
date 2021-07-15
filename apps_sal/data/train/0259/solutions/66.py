class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        a = 1
        b = max(nums)
        i = (a+b)//2
        ans = 10000000000000
        while b-a >1:
            sum = 0
            for j in nums:
                if j%i == 0:
                    sum += j//i
                else:
                    sum += j//i + 1
            if sum <= threshold:
                ans = min(i,ans)
                b = i
            else:
                a = i
            i = (a+b)//2
        for i in(a,b):
            sum = 0
            for j in nums:
                if j%i == 0:
                    sum += j//i
                else:
                    sum += j//i + 1
            if sum <= threshold:
                ans = min(i,ans)  
        return ans
