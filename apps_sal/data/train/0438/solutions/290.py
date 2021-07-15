class Solution:
    # https://leetcode.com/problems/find-latest-group-of-size-m/discuss/806786/JavaC%2B%2BPython-Count-the-Length-of-Groups-O(N)
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        length = [0 for _ in range(len(arr) + 2)]
        res = -1
        # n starts from 1.
        for i, n in enumerate(arr):
            left, right = length[n - 1], length[n + 1]
            if left == m or right == m:
                #update res for each time satisfying conditiong. so return the latest one.
                res = i
            # update edge. [0111010], change middle 0 t0 1. left = 3, right = 1.total length = 3 + 1 + 1 = 5. edge, length[1] = 5, length[6] = 5
            length[n - left] = length[n + right] = left + right + 1
        return res
            

