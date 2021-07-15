import math
n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(10 ** 9)
    return
l = [0] * n
r = [0] * n
l[0] = a[0]
r[-1] = a[-1]
for i in range(n-1):
    l[i+1] = math.gcd(a[i+1], l[i])
    r[-i-2] = math.gcd(a[-i-2], r[-i-1])
ans = max(l[-2], r[1])
for i in range(n-2):
    ans = max(ans, math.gcd(l[i], r[i+2]))
print(ans)
