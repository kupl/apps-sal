class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        count = collections.Counter(nums)
        
        for n in nums: #loop all the numbers
            
            if count[n] != 0: #base condition whre count[n] is null means no need to continue the loop

                for v in range(n, n + k): #each num in num if it is in count dict then. loop for 4 nums
                    count[v] -= 1
                    if count[v] < 0:
                        return False
                    
        return True

