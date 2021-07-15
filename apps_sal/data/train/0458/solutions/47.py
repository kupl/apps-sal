class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sumtot=sum(nums)
        sumtot%=p
        if not sumtot:
            return 0
        
        sums=collections.defaultdict(int)
        sums[0]=-1
        sumtill=0
        result=float('inf')
        
        for i,num in enumerate(nums):
            sumtill+=num
            sumtill%=p
            diff=(sumtill-sumtot)%p
            if diff in sums:
                result=min(result,i-sums[diff])
            
            sums[sumtill]=i
            
        if result==float('inf') or result==len(nums):
            return -1
        else:
            return result

