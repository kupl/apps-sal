class Solution:
    # O(N*M) Solution
    def numTriplets(self, nums1, nums2):
        res = 0
        for n in nums1:
            res += self.twoProduct(n * n, nums2)
        for n in nums2:
            res += self.twoProduct(n * n, nums1)

        return res

    def twoProduct(self, target, nums):
        count = 0
        compFreq = {}  # key: compliment (target/cur), element: freq of this compliment (NOT idx!!!)
        cList = set()
        for i in range(len(nums)):
            comp = target / nums[i]
            if comp == int(comp):  # is comp is a float, no need to proceed
                if nums[i] in compFreq:
                    count += compFreq[nums[i]]

                if comp in compFreq:  # update freq
                    compFreq[comp] += 1
                else:
                    compFreq[comp] = 1
        return count

    '''
    # O(N^2) Solution
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int: 
        res = 0
        
        # freq is dict that has key=n^2, element=frequency of n^2 occur
        # if there are duplicate in nums1=[2,2], and nums2=[1,4], there are 2 cases in stead on 1
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
