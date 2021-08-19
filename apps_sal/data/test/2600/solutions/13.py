import sys


def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    Z = [0] * (n + m - 1)
    O = [0] * (n + m - 1)
    for i in range(n):
        A = [int(j) for j in input().split()]
        for (j, a) in enumerate(A):
            if a == 0:
                Z[i + j] += 1
            else:
                O[i + j] += 1
    ans = 0
    for i in range((n + m - 1) // 2):
        (x, y) = (Z[i] + Z[n + m - 2 - i], O[i] + O[n + m - 2 - i])
        ans += min(x, y)
    print(ans)
