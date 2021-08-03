class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == 1:
            return 1
        dic, groups = {i: 0 for i in range(1, n + 1)}, {i: 0 for i in range(1, n + 1)}
        right = {i: 0 for i in range(1, n + 1)}
        laststep = -1
        for idx, i in enumerate(arr):
            # single 1
            if (i == 1 or dic[i - 1] == 0) and (i == n or dic[i + 1] == 0):
                groups[1] += 1
                dic[i] = i
                right[i] = i
            # add 1 to right
            elif (i == n or dic[i + 1] == 0) and (i > 0 and dic[i - 1] > 0):
                leftmost = dic[i - 1]
                dic[i] = leftmost
                right[leftmost] = i
                right[i] = i
                groups[i - leftmost] -= 1
                groups[i - leftmost + 1] += 1
            # add 1 to left
            elif (i == 1 or dic[i - 1] == 0) and (i < n and dic[i + 1] > 0):
                rightmost = right[i + 1]
                dic[rightmost] = i
                dic[i] = i
                right[i] = rightmost
                groups[rightmost - i] -= 1
                groups[rightmost - i + 1] += 1
            else:
                leftmost = dic[i - 1]
                rightmost = right[i + 1]
                right[leftmost] = rightmost
                dic[rightmost] = leftmost
                groups[rightmost - i] -= 1
                groups[i - leftmost] -= 1
                groups[rightmost - leftmost + 1] += 1

            if groups[m] > 0:
                laststep = idx + 1
            # print(\"step:\", idx+1, \":\",groups)
        return laststep
