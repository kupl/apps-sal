class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        g_right = {}
        g_left = {}
        lengths = [0] * n  # number of cells with length 1, 2, ... , n
        res = -1
        for itr, i in enumerate(arr):
            pos = i - 1
            rb = i - 1
            lb = i - 1

            if pos + 1 in g_right:
                rb = g_right[pos + 1]
                end = g_right.pop(pos + 1)
                lengths[end - (pos + 1)] -= 1

            if pos - 1 in g_left:
                lb = g_left[pos - 1]
                end = g_left.pop(pos - 1)
                lengths[(pos - 1) - end] -= 1

            g_left.update({rb: lb})
            g_right.update({lb: rb})
            lengths[rb - lb] += 1
            # print(lengths)
            if lengths[m - 1] > 0:
                res = itr + 1

        return res
        #     for i in g_
        #     if m in s:
        #         res = itr + 1
        # return res
