class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        count1=0
        rt=[]
        while(count1<len(nums)):
            count2=len(nums)-1
            while(count2>=count1):
               
                sum2=sum(nums[count1:count2+1])
                rt.append(sum2)
                count2=count2-1
            count1=count1+1
        rt.sort()
        a=pow(10,9)+7
        if sum(rt[left-1:right]) > pow(10,9)+7:
            return sum(rt[left-1:right])%1000000007
        else:
            return sum(rt[left-1:right])

