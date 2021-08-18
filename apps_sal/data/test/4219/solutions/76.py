import sys
from itertools import chain
from itertools import product


def check(N, ptn, m_assert):
    for i in range(N):
        if ptn[i] == 1:
            for j in range(i + 1, N):
                if ptn[j] == 1:
                    if m_assert[i][j] == 0:
                        return False
                    if m_assert[j][i] == 0:
                        return False
                else:
                    if m_assert[i][j] == 1:
                        return False
        else:
            for j in range(i + 1, N):
                if ptn[j] == 1:
                    if m_assert[j][i] == 1:
                        return False
    return True


def solve(N, m_assert):
    ans = 0
    for ptn in product([1, 0], repeat=N):
        if check(N, ptn, m_assert):
            ans = max(sum(ptn), ans)
    return ans


def main():
    N = int(input())
    m_assert = [[-1] * N for _ in range(N)]
    for n in range(N):
        A = int(input())
        for a in range(A):
            x, y = list(map(int, input().split()))
            m_assert[n][x - 1] = y
    answer = solve(N, m_assert)
    print(answer)


def __starting_point():
    main()


__starting_point()
