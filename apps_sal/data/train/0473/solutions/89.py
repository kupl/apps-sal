class Solution:
    def countTriplets(self, arr: List[int]) -> int:   
        def get_triplets(nums):
            n = len(nums)
            triplets = 0
            i = 0
            while i < n - 1:
                lsum = nums[i]
                j = i + 1
                while j < n:
                    k = j
                    rsum = nums[j]
                    while k < n:
                        if lsum == rsum: triplets += 1
                        k += 1
                        if k < n: rsum = rsum ^ nums[k]
                    j += 1
                    lsum = lsum ^ nums[j - 1]
                i += 1
            
            return triplets
        
        return get_triplets(arr)

