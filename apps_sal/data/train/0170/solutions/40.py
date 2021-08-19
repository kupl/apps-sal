import bisect


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        s = {}
        a = [(arr[0], 0)]
        s[0] = (0, 0)
        n = len(arr)
        for i in range(1, n):
            if s[i - 1][1] == 0:
                move = 1
            else:
                move = s[i - 1][0] + 1
            index = bisect.bisect_right(a, (arr[i], i))
            if index == 0:
                nmove = i
            else:
                nmove = i - a[index - 1][1] - 1
            if arr[i - 1] <= arr[i]:
                nmove = min(nmove, s[i - 1][1])
            if nmove == 0:
                bisect.insort_right(a, (arr[i], i))
            s[i] = (move, nmove)
            # print(s)
        return min(s[n - 1][0], s[n - 1][1])
