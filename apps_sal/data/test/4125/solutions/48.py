from math import gcd

N, X = list(map(int, input().split()))
xs = list(map(int, input().split()))

aX = list([abs(x-X) for x in xs])

ans = aX[0]
for i in range(1, N):
    ans = gcd(ans, aX[i])
print(ans)

