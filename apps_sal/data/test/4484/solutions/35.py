import math
a,b=map(int, input().split())

if abs(a-b) == 1:
    c = math.factorial(a)%(10**9+7)
    d = math.factorial(b)%(10**9+7)
    print(c*d%(10**9+7))
if abs(a-b) == 0:
    c = math.factorial(a)%(10**9+7)
    d = math.factorial(b)%(10**9+7)
    print(c*d*2%(10**9+7))
if abs(a-b) >= 2:
    print(0)
