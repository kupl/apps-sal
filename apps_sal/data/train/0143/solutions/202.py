class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, nums, ans = 0, collections.Counter(), 0
        for r in range(len(tree)):
            nums[tree[r]] += 1
            while len(nums) > 2:
                nums[tree[l]] -= 1
                if not nums[tree[l]]:
                    del nums[tree[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
                    
                    
                

