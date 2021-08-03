class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        l = len(arr)
        left = [i for i in range(l + 1)]
        right = [i for i in range(l + 2)]
        count = [0] * (l + 1)
        res = -1
        step = 0
        for a in arr:
            step += 1
            lt = left[a - 1]
            rt = right[a + 1]
            tlen = rt - lt - 1

            templeft = a - lt - 1
            tempright = rt - a - 1
            count[templeft] -= 1
            count[tempright] -= 1
            count[tlen] += 1

            if count[m] > 0:
                res = step
            right[lt + 1] = rt
            left[rt - 1] = lt
        return res
