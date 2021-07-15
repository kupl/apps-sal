class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        S = sum(nums)
        if S%3==0: return S
        
        ns1 = sorted([n for n in nums if n%3==1])
        ns2 = sorted([n for n in nums if n%3==2])
        
        remove = S
        
        if ([[],ns1,ns2][S%3]):
            remove = min(remove, [[],ns1,ns2][S%3][0])
        if len([[],ns1,ns2][3-S%3])>1:
            remove = min(remove, sum([[],ns1,ns2][3-S%3][:2]))
        
        return S - remove
