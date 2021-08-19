import numpy


class Solution:

    def makeNewArray(self, num: List[int], breakpoint: List[int]):
        result = []
        flag = False
        bp_cur = 0
        sum = 0
        for index, value in enumerate(num):
            if bp_cur < len(breakpoint) and index == breakpoint[bp_cur]:
                if flag:
                    result.append(sum)
                else:
                    result.append(0)

                flag = False
                sum = 0
                result.append(value)
                bp_cur += 1
            else:
                sum += value
                flag = True

        if flag:
            result.append(sum)
        else:
            result.append(0)

        return result

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        result = 0
        cur0 = 0
        cur1 = 0
        bp0 = []
        bp1 = []
        while cur0 < len(nums1) and cur1 < len(nums2):
            if nums1[cur0] == nums2[cur1]:
                bp0.append(cur0)
                bp1.append(cur1)
                cur0 += 1
                cur1 += 1
            elif nums1[cur0] < nums2[cur1]:
                cur0 += 1
            else:
                cur1 += 1

        # print(\"[dbg] the breakpoint for arr0 is: \", bp0)
        new_arr0 = self.makeNewArray(nums1, bp0)
        # print(\"[dbg] the new array for arr1 is: \", new_arr0)

        # print(\"[dbg] the breakpoint for arr1 is: \", bp1)
        new_arr1 = self.makeNewArray(nums2, bp1)
        # print(\"[dbg] the new array for arr2 is: \", new_arr1)

        dim = (len(new_arr0), 2)
        dp = numpy.zeros(dim)

        dp[0][0] = new_arr0[0]
        dp[0][1] = new_arr1[0]

        # print(\"[dbg] the new len0:\", len(new_arr0))
        # print(\"[dbg] the new len1:\", len(new_arr1))

        for dx in range(1, len(new_arr1)):
            dp[dx][0] = max(dp[dx - 1][0], dp[dx - 1][1]) + new_arr0[dx]
            dp[dx][1] = max(dp[dx - 1][0], dp[dx - 1][1]) + new_arr1[dx]

        module = int(pow(10, 9) + 7)
        return int(max(dp[-1][0], dp[-1][1])) % module
