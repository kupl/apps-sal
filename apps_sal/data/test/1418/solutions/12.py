import sys
input = sys.stdin.readline


class Problem:
    def __init__(self):
        pass

    def solve(self):
        print(self._solve())

    def _solve(self):
        n = int(input())
        done = [0] * (n + 1)
        v = 1
        for i in range(2, n + 1):
            if done[i]:
                continue
            k = 1
            while k * i <= n:
                done[k * i] = v
                k += 1
            v += 1

        return ' '.join(str(x) for x in done[2:])


def main():
    problem = Problem()
    problem.solve()


def __starting_point():
    main()


__starting_point()
