import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    one = [0] * (n + m - 1)
    zero = [0] * (n + m - 1)
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(m):
            one[i + j] += (a[j] == 1)
            zero[i + j] += (a[j] == 0)

    res = 0
    for i in range((n + m - 1) // 2):
        s = one[i] + one[n + m - 2 - i]
        t = zero[i] + zero[n + m - 2 - i]
        res += min(s, t)
    print(res)
