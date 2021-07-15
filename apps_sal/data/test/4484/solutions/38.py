import math
n,m = map(int,input().split())

x = 10**9+7

ans = 0
if n == m:
    ans += math.factorial(n) * math.factorial(m) * 2
    print(ans % x)
    return
elif n >= m and n -m == 1:
    ans += math.factorial(n) * math.factorial(m)
    print(ans % x)
    return
elif m >= n and m -n== 1:
    ans += math.factorial(n) * math.factorial(m)
    print(ans % x)
    return
else:
    print(ans % x)
