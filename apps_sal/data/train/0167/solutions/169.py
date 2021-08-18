class Solution:
    def __init__(self):
        self.memo = {}

    def superEggDrop(self, K: int, N: int) -> int:

        def solve(K, N):
            d = self.memo.get((K, N))

            if d is None:
                if K == 1 or N <= 2:
                    d = N

                else:
                    A_min = 1
                    A_max = N

                    while A_max - A_min > 1:
                        A = (A_min + A_max) // 2
                        t1 = solve(K - 1, A - 1)
                        t2 = solve(K, N - A)

                        if t1 > t2:
                            A_max = A
                        elif t2 > t1:
                            A_min = A
                        else:
                            A_min = A_max = A

                    d = 1 + min(
                        max(
                            self.memo[K - 1, A - 1],
                            self.memo[K, N - A]
                        )
                        for A in [A_min, A_max]
                    )

                self.memo[K, N] = d

            return d

        return solve(K, N)
