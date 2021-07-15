class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        x=sum(nums)
        if x%3==0:
            return x
        nums.sort()
        #print(nums,x)
        opt1=10**4+1
        opt2=count=0
        for n in nums:
            if n%3==x%3:
                opt1=min(opt1, n)
                if count==2:
                    break
            elif n%3!=0 and n%3!=x%3:
                if count<=1:
                    opt2+=n
                    count+=1
                elif count==2:
                    pass
        #print(opt1, opt2)
        if count==2:
            return x-min(opt1,opt2)
        return x-opt1
