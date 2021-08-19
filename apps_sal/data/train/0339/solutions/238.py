class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        for num1 in nums1:
            a = num1 * num1
            hashSet = defaultdict(int)
            for num2 in nums2:
                complement = a / num2
                if complement in hashSet:
                    count += hashSet[complement]
                hashSet[num2] += 1
        for num2 in nums2:
            a = num2 * num2
            hashSet = defaultdict(int)
            for num1 in nums1:
                complement = a / num1
                if complement in hashSet:
                    count += hashSet[complement]
                hashSet[num1] += 1
        return count
