import math


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dict = {}
    dict[0] = 1
    (sum, ans) = (0, 0)
    for i in range(0, n):
        sum += a[i]
        if sum in list(dict.keys()):
            ans += 1
            dict = {}
            dict[0] = 1
            sum = a[i]
            dict[sum] = 1
        else:
            dict[sum] = 1
    print(ans)


t = 1
for _ in range(0, t):
    solve()
