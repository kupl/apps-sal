class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        presum = []
        presum.append(nums[0])
        for i in range(1,len(nums)):
            presum.append(nums[i]+presum[i-1])
        # print(presum)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i==j:
                    sums.append(nums[i])
                else:
                    if i == 0:
                        sums.append(presum[j])
                    else:
                        sums.append(presum[j] - presum[i-1])
        sums = sorted(sums)
        # print(sums)
        return sum(sums[left-1:right])%((10**9)+7)
