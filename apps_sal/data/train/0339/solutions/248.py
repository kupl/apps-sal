class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            target = [i**2 for i in nums1]
            ans = 0
            for i in range(len(target)): 
                s = target[i]
                d = collections.defaultdict(list)
                for j in range(len(nums2)):
                    if nums2[j] in d: ans += len(d[nums2[j]])
                    d[s/nums2[j]].append(j)
            #print(ans)            
            return ans
        return helper(nums1, nums2) + helper(nums2, nums1)

