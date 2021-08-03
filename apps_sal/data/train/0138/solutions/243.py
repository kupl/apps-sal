class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        arrs = [[]]
        for i in nums:
            if i:
                arrs[-1].append(i)
            else:
                arrs.append([])
        ans = 0
        for arr in arrs:
            if not len(arr):
                continue
            negs = 0
            for i in arr:
                if i < 0:
                    negs += 1
            if negs % 2:
                p1 = 0
                while arr[p1] > 0:
                    p1 += 1
                p2 = len(arr) - 1
                while arr[p2] > 0:
                    p2 -= 1
                ans = max(len(arr) - p1 - 1, p2, ans)
            else:
                ans = max(ans, len(arr))
        return ans
