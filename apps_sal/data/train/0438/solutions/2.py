class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        sizes = [0] * (len(arr) + 2)
        res = -1
        cnt = 0
        for (step, cur) in enumerate(arr, start=1):
            (l, r) = (sizes[cur - 1], sizes[cur + 1])
            new_sz = l + 1 + r
            sizes[cur - l] = sizes[cur + r] = new_sz
            if l == m:
                cnt -= 1
            if r == m:
                cnt -= 1
            if new_sz == m:
                cnt += 1
            if cnt:
                res = step
        return res
