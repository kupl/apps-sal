class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        one = [i**2 for i in nums1]
        two = [j**2 for j in nums2]
        self.cnt = 0
        d1 = collections.defaultdict(int)
        self.calculate(one,nums2)
        self.calculate(two,nums1)
        return self.cnt
    def calculate(self,square,nums):
        for i in range(len(square)):
            target = square[i]
            d = collections.defaultdict(list)
            for j in range(len(nums)):
                if target%nums[j]==0 and int(target/nums[j]) in d:
                    # print(target,nums[j],d[nums[j]])
                    self.cnt+=len(d[target/nums[j]])
                d[nums[j]].append(j)
                # print(target,d)

