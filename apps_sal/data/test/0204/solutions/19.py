"""
N=int(input())
s=[int(x) for x in input().split()]
mn=min(s)
mx=max(s)
diff=mx-mn+1
ans=diff-len(s)
print(ans)


import math
a, b, x, y = list(map(int, input().split()))
g = math.gcd(x, y)
x = x // g
y = y // g
a1 = a // x
a2 = b // y
ans = min(a1, a2)
print(ans)
