class Solution:
    def numTripletsHelper(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_map = {}
        count = 0

        for i in nums1:
            if i in nums1_map:
                nums1_map[i] += 1
            else:
                nums1_map[i] = 1
        
        for i in nums2:
            i_2 = i * i
            seen = set({})
            for j in nums1:
                left = nums1_map[j]
                if i_2 / j == j:
                    if (j, j) not in seen and left > 1:
                        count += int((left * (left - 1)) / 2)
                        seen.add((j, j))
                elif i_2 / j in nums1_map and (int(i_2 / j), j) not in seen:
                    right = nums1_map[i_2 / j]
                    seen.add((int(i_2 / j), j))
                    seen.add((j, int(i_2 / j)))
                    count += left * right
        
        return count
        
    
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.numTripletsHelper(nums1, nums2) + self.numTripletsHelper(nums2, nums1)
