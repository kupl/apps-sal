import sys

input = sys.stdin.readline


def pyramid(n, l, r):
    if l == r:
        return l
    mid = (l + r + 1) // 2
    if (3 * mid * mid + mid) // 2 > n:
        return pyramid(n, l, mid - 1)
    else:
        return pyramid(n, mid, r)

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n >= 2:
        x = pyramid(n, 1, n)
        n -= (3 * x * x + x) // 2
        cnt += 1
    print(cnt)

