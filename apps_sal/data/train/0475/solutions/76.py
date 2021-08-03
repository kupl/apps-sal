class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ss = [x for x in nums]  # ss is the subarray sums of nums
        for idi, i in enumerate(nums):
            si = i  # si is a sum of subarray(s) that includes i
            for j in nums[idi + 1:]:
                si += j
                ss.append(si)
        ss.sort()
        return sum(ss[left - 1:right]) % 1000000007
