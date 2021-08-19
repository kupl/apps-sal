import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    (cur, level, add) = (0, 0, 1)
    k -= 1
    while k >= cur + add:
        cur += add
        level += 1
        add += 1
    (x, y) = (n - 2 - level, n - 1 - (k - cur))
    ans = ['a' for _ in range(n)]
    (ans[x], ans[y]) = ('b', 'b')
    print(''.join(ans))
