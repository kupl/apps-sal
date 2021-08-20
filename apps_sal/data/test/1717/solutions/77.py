from math import gcd


def resolve():
    n = int(input())
    ans = 1
    for i in range(1, n + 1):
        ans = i * ans // gcd(i, ans)
    print(ans + 1)


resolve()
