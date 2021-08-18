class Solution:
    def numTriplets(self, nums1, nums2):
        res = 0
        for n in nums1:
            res += self.twoProduct(n * n, nums2)
        for n in nums2:
            res += self.twoProduct(n * n, nums1)

        return res

    def twoProduct(self, target, nums):
        count = 0
        compFreq = {}
        cList = set()
        for i in range(len(nums)):
            comp = target / nums[i]
            if comp == int(comp):
                if nums[i] in compFreq:
                    count += compFreq[nums[i]]

                if comp in compFreq:
                    compFreq[comp] += 1
                else:
                    compFreq[comp] = 1
        return count

    '''
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int: 
        res = 0
        
        freq1 = {}
        freq2 = {}
        for n in nums1:
            if n*n in freq1:
                freq1[n*n] += 1
            else:
                freq1[n*n] = 1
        for n in nums2:
            if n*n in freq2:
                freq2[n*n] += 1
            else:
                freq2[n*n] = 1
        
        for b in range(len(nums2)-1):
            for c in range(b+1, len(nums2)):
                if (nums2[b] * nums2[c]) in freq1:
                    res += freq1[nums2[b] * nums2[c]]
                    
        for b in range(len(nums1)-1):
            for c in range(b+1, len(nums1)):
                if (nums1[b] * nums1[c]) in freq2:
                    res += freq2[nums1[b] * nums1[c]]
        return res
    '''
