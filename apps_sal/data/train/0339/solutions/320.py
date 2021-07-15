class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def twoProduct(target, nums) -> int:
            goal = defaultdict(list)
            tot = 0
            for i in range(len(nums)):
                if len(goal[nums[i]]) != 0:
                    tot += len(goal[nums[i]])
                goal[target/(nums[i])].append(i)
            
            return tot
        
        count = 0
        for n in nums1:
            count += twoProduct(n*n, nums2)
        
        for n in nums2:
            count += twoProduct(n*n, nums1)
        
        return count
