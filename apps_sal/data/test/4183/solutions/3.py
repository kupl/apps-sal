import math

n = int(input())
tl = list(int(input()) for _ in range(n))

if n == 1:
    print(tl[0])
else:
    ans = tl[0]
    for i in range(1, n):
        ans = ans // math.gcd(ans, tl[i]) * tl[i]

    print(ans)
