class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        return self.recur(n, -1, 1, rollMax, {}) % (10**9 + 7)

    def recur(self, n, prev, count, rollMax, op):

        if (n, prev, count) in op:
            return op[(n, prev, count)]

        if n == 0:
            return 1
        else:

            t = 0
            for i in range(6):

                if prev == i:
                    if count + 1 <= rollMax[i]:
                        t += self.recur(n - 1, i, count + 1, rollMax, op)

                else:

                    t += self.recur(n - 1, i, 1, rollMax, op)

            op[(n, prev, count)] = t
            return t
