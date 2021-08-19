class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l = r = 0
        s = arr[l]
        res = []
        while r < len(arr):
            if s == target:
                ln = r - l + 1
                res.append((ln, l, r))

            if s <= target:
                r += 1
                if r < len(arr):
                    s += arr[r]
            else:
                l += 1
                s -= arr[l - 1]
                if l > r:
                    r += 1
                    if r < len(arr):
                        s += arr[r]

        msl = [math.inf] * len(arr)  # minimum interval length so far from left
        msr = [math.inf] * len(arr)  # minimum interval length so far fromm right

        mi = math.inf
        resi = -1
        for i in range(len(arr)):
            if resi + 1 < len(res) and res[resi + 1][2] == i:
                resi += 1
                mi = min(mi, res[resi][0])
            msl[i] = mi

        mi = math.inf
        resi = len(res)
        for i in range(len(arr) - 1, -1, -1):
            if resi - 1 >= 0 and res[resi - 1][1] == i:
                resi -= 1
                mi = min(mi, res[resi][0])
            msr[i] = mi

        mn = math.inf
        for i in range(len(arr) - 1):
            mn = min(mn, msl[i] + msr[i + 1])

        if mn == math.inf:
            return -1
        return mn
