class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        list_N = list(map(int, str(N + 1)))
        solution = 0

        def permutation(m, n):
            return 1 if n == 0 else permutation(m, n - 1) * (m - n + 1)
        for i in range(1, len(list_N)):
            solution += 9 * permutation(9, i - 1)
        seen_set = set()
        for i, x in enumerate(list_N):
            for y in range(0 if i else 1, x):
                if y not in seen_set:
                    solution += permutation(9 - i, len(list_N) - i - 1)
            if x in seen_set:
                break
            seen_set.add(x)
        return N - solution
