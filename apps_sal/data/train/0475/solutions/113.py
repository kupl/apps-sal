class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        (i, j, amt) = (0, 0, 0)
        total = []
        while i < n:
            if j == n - 1:
                amt += nums[j]
                total.append(amt)
                i += 1
                j = i
                amt = 0
            elif i == j:
                amt = nums[j]
                total.append(amt)
                j += 1
            else:
                amt += nums[j]
                total.append(amt)
                j += 1
        total.sort()
        return sum(total[left - 1:right]) % (10 ** 9 + 7)
