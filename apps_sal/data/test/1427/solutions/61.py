import math
n = int(input())
a = list(map(int, input().split()))
s = a[0]
for i in a[1:]:
    s = (s*i)//math.gcd(s,i)
num = 0
for h in a:
    num += (s//h)
print(num%((10**9)+7))
