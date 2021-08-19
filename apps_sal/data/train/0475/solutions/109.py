class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        1.构造函数求前k个子数组的和
        2.目标就是求前right个子数组和减去前left-1个子数组和
        3.构造函数求所有<=m的子数组的数目以及这些子数组的和
        """

        def countandsum(target):
            i = 0
            cur = 0
            sum1 = 0
            total = 0
            count = 0
            for j in range(n):
                cur += nums[j]
                sum1 += nums[j] * (j - i + 1)
                while cur > target:
                    sum1 -= cur
                    cur -= nums[i]
                    i += 1
                count += j - i + 1
                total += sum1
            return [count, total]

        def sumk(k):
            l = min(nums)
            r = sum(nums)
            while l < r:
                m = (l + r) // 2
                if countandsum(m)[0] < k:
                    l = m + 1
                else:
                    r = m
            (count, total) = countandsum(l)
            return total - l * (count - k)
        return (sumk(right) - sumk(left - 1)) % (10 ** 9 + 7)
