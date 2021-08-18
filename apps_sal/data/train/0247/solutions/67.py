class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left = list(itertools.accumulate(arr))
        right = list(itertools.accumulate(arr[::-1]))
        right = right[::-1]

        rans = [500000] * len(arr)
        lans = [500000] * len(arr)

        i, j, n = 0, 0, len(arr)

        while i < n and j < n:
            sm = left[j] - (left[i - 1] if i else 0)
            while sm > target and i <= j:
                i += 1
                sm = left[j] - (left[i - 1] if i else 0)

            if sm == target:
                lans[j] = min(lans[j], j - i + 1)

            j += 1

        i, j = n - 1, n - 1
        while i > -1:
            sm = right[i] - (right[j + 1] if (j + 1 < n) else 0)

            while sm > target and j >= i:
                j -= 1
                sm = right[i] - (right[j + 1] if (j + 1 < n) else 0)

            if sm == target:
                rans[i] = min(rans[i], j - i + 1)
            i -= 1

        ans = math.inf
        mv = 999999999
        for i in range(n):
            mv = min(mv, lans[i])
            lans[i] = mv

        mv = 212498174
        for i in range(n - 1, -1, -1):
            mv = min(mv, rans[i])
            rans[i] = mv

        for i in range(n - 1):
            ans = min(ans, lans[i] + rans[i + 1])

        return ans if ans < 500000 else -1
