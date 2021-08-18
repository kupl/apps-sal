import sys
from fractions import gcd
n, x, d = map(int, input().split())
"""
数列からi個選ぶことを考えると
i*xに加えて足されるdの数はi(i-1)/2 〜 i(2n-1-i)/2 の任意の個数
i > j なるjで代替されるような和はこのうちどのような条件を満たすものか？
g = gcd(x, d). l = lcm(x, d)として
(g*l = x*d)
i*x + k*d が条件を満たすとすると
i*x + k*d = (i - d/g)x + (k + x/g)d が成り立つ
(i - d/g)(2n - 1 - i + d/g)/2 >= (k + x/g) となるような最大のkを求めれば，
k以下はすべてかぶる，k+1以上はすべてかぶらない

x<0 のときは
(i - d//g) * (i - d//g - 1)//2 <= (k + x//g) <= (i - d//g) * (2*n - 1 - i + d//g)//2
(i - d//g) * (i - d//g - 1)//2 - x//g <= k <= (i - d//g) * (2*n - 1 - i + d//g)//2 - x//g
となるようなkにおいてはかぶる
"""
if x == 0 and d == 0:
    print(1)
    return
elif d == 0:
    print(n + 1)
    return

if x < 0 and x + (n - 1) * d < 0:
    x, d = -x, -d

if x >= 0 and d < 0:
    x, d = x + (n - 1) * d, -d

#print(x, d)
g = gcd(x, d)

ans = 1
if x >= 0:
    for i in range(1, n + 1):
        #print((i - d//g) * (2*n - 1 - i + d//g) // 2 - x//g)
        k = max((i - d // g) * (2 * n - 1 - i + d // g) // 2 - x // g, i * (i - 1) // 2 - 1)
        # print(k)
        ans += max((i * (2 * n - 1 - i)) // 2 - k, 0)

else:
    for i in range(1, n + 1):
        overlap_u = min((i - d // g) * (2 * n - 1 - i + d // g) // 2 - x // g, i * (2 * n - 1 - i) // 2)
        overlap_l = max((i - d // g) * (i - d // g - 1) // 2 - x // g, i * (i - 1) // 2)
        ans += i * (2 * n - 1 - i) // 2 - i * (i - 1) // 2 + 1 - max(overlap_u - overlap_l + 1, 0)

print(ans)
