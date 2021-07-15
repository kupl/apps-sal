class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        base = sum([abs(nums[i] - nums[i+1]) for i in range(n - 1)])
        if (n <= 2):
            return base
        
        #best = base
        #for i in range(n-1):
        #    for j in range(i+1, n):
        #        guess = switch(nums, i, j, base)
        #        if guess > best:
        #            best = guess
        
        inds = sorted(list(range(n)), key=lambda x: nums[x])
        return base + max(options(inds, nums))
        
    
def switch(nums, i, j, base=0):
    i_inc = ((abs(nums[j] - nums[i-1]) - abs(nums[i] - nums[i-1])) if (i > 0) else 0)
    j_inc = ((abs(nums[j+1] - nums[i]) - abs(nums[j+1] - nums[j])) if (j < len(nums) - 1) else 0)
    return base + i_inc + j_inc
    
    

def options(inds, nums):
    a,b = findRange(inds)
    d,c = findRange(inds[::-1])
    yield 0
    yield 2 * (nums[c] - nums[b])

    i = max(a, b)
    j = max(c, d)
    n = len(nums)
    yield switch(nums, i, n-1)
    yield switch(nums, j, n-1)
    
    yield switch(nums, 0, i-1)
    yield switch(nums, 0, j-1)
    
    
    
    

def findRange(inds):
    seen = set()
    for i, idx in enumerate(inds):
        if (idx + 1) in seen or (idx - 1) in seen:
            return (idx + 1, idx) if (idx + 1) in seen else (idx-1, idx)
        seen.add(idx)
        

