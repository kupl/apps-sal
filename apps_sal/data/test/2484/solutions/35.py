import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: "List[int]"):
    ans = 0
    j = 0
    x = 0
    for i in range(N):
        while j < N and (x & A[j]) == 0:
            x ^= A[j]
            j += 1
        ans += j - i
        x ^= A[i]
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    solve(N, A)


def __starting_point():
    main()


__starting_point()
