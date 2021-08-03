from collections import defaultdict as d


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # define a range as [l,r]
        left = dict()  # left[r]=l
        right = dict()  # right[l]=r
        cntLengths = d(lambda: 0)  # cntLengths[length]=cnts
        ans = -1
        for i in range(len(arr)):
            num = arr[i]
            lower = num
            upper = num

            if num + 1 in right.keys():
                upper = right[num + 1]
                right.pop(num + 1)
                cntLengths[upper - num] -= 1
            if num - 1 in left.keys():
                lower = left[num - 1]
                left.pop(num - 1)
                cntLengths[num - lower] -= 1
            left[upper] = lower
            right[lower] = upper
            cntLengths[upper - lower + 1] += 1

            if cntLengths[m] > 0:
                ans = i + 1

        return ans
