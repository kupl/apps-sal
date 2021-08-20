import sys
input = sys.stdin.readline
(N, A, B, C) = map(int, input().split())
L = [int(input()) for i in range(N)]
INF = float('inf')


def dfs(i, a, b, c):
    if i == N:
        if a == 0 or b == 0 or c == 0:
            return INF
        else:
            return abs(a - A) + abs(b - B) + abs(c - C)
    ans0 = dfs(i + 1, a, b, c)
    ans1 = dfs(i + 1, a + L[i], b, c) + (10 if a != 0 else 0)
    ans2 = dfs(i + 1, a, b + L[i], c) + (10 if b != 0 else 0)
    ans3 = dfs(i + 1, a, b, c + L[i]) + (10 if c != 0 else 0)
    ans = min(ans0, ans1, ans2, ans3)
    return ans


def main():
    print(dfs(0, 0, 0, 0))


def __starting_point():
    main()


__starting_point()
