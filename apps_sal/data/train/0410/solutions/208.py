class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        if lo == 1 and hi == 1 and k == 1:
            return 1

        memo = {}

        def count_steps(x, count, memo):
            if x == 1:
                return count
            count += 1
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1

            if x in memo:
                return count + memo[x]

            return count_steps(x, count, memo)

        for x in range(lo, hi + 1):
            memo[x] = count_steps(x, 0, memo)

        return sorted(memo.items(), key=lambda x: x[1])[k - 1][0]
