class Solution:

    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        n = len(A)
        mtr = [[0 for i in range(n + 1)] for j in range(k + 1)]

        def rec(parts, arrIndex):
            if mtr[parts][arrIndex] != 0:
                return mtr[parts][arrIndex]
            if parts == 1:
                mtr[parts][arrIndex] = sum(A[:arrIndex + 1]) / (arrIndex + 1)
                return mtr[parts][arrIndex]
            for x in range(1, arrIndex + 1):
                mtr[parts][arrIndex] = max(mtr[parts][arrIndex], rec(parts - 1, x - 1) + sum(A[x:arrIndex + 1]) / (arrIndex + 1 - x))
            return mtr[parts][arrIndex]
        rec(k, n - 1)
        ans = sys.maxsize * -1
        for i in range(1, k + 1):
            ans = max(ans, mtr[i][-2])
        return ans
