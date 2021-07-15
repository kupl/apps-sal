import math
n,m = map(int, input().split())
a = math.factorial(m)
b = math.factorial(n)
if 1 < abs(n-m):
    print(0)
elif abs(n-m) == 0:
    print((a*b*2)%1000000007)
elif abs(m-n) == 1:
    print((a*b)%1000000007)
