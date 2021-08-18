from sortedcontainers import SortedDict


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return 1
        dp_even, dp_odd = [False] * (n + 1), [False] * (n + 1)

        dp_even[n - 1] = dp_odd[n - 1] = True
        sortedDict = SortedDict({A[n - 1]: n - 1})
        for i in reversed(range(n - 1)):
            num = A[i]
            lower = sortedDict.bisect_right(num)
            lower = sortedDict[sortedDict.keys()[lower - 1]] if lower else -1
            higher = sortedDict.bisect_left(num)
            higher = -1 if higher == len(sortedDict) else sortedDict[sortedDict.keys()[higher]]
            sortedDict[num] = i
            dp_even[i] = dp_odd[lower]
            dp_odd[i] = dp_even[higher]
        return dp_odd.count(True)
