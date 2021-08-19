class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        acc = 0
        for i in nums:
            acc += i
            sums.append(acc)
        allsums = []
        while sums:
            allsums.extend(sums)
            sums = list([x - sums[0] for x in sums[1:]])
        allsums.sort()
        return sum(allsums[left - 1:right]) % (10 ** 9 + 7)
