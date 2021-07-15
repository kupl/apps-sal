import math
N = int(input())
a = list(map(int,input().split()))

s = sum(a)
t = 0
minimum = math.inf
for i in range(N-1):
    t += a[i]
    s -= a[i]
    minimum = min(minimum,abs(s-t))
print(minimum)
