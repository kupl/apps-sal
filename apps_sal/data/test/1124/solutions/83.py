from math import gcd

N = int(input())
a = list(map(int, input().split()))

if N == 1:
    print((a[0]))
    return

ans = gcd(a[0], a[1])
if N == 2:
    print(ans)
    return
for i in range(2, N):
    ans = gcd(ans, a[i])
print(ans)
