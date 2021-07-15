class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        pos = [None] * (len(arr) + 3)
        num = 0
        ans = -1
        for idx in range(1, len(arr) + 1):
            l, r, p = [arr[idx - 1]] * 3
            if pos[p-1]:
                if pos[p-1][1] - pos[p-1][0] + 1 == m:
                    num -= 1
                l = pos[p-1][0]
            if pos[p + 1]:
                if pos[p + 1][1] - pos[p+1][0] + 1 == m:
                    num -= 1
                r = pos[p+1][1]
            pos[l] = pos[r] = (l, r)
            if r - l + 1 == m:
                num += 1
            if num != 0:
                ans = idx
        return ans
