import math
n = int(input())
a = [0]*n
b = [0]*n
for i in range(n):
  a[i], b[i] = list(map(int, input().split()))
a.sort()
b.sort()
ans = 0
h = int(n/2)
if n % 2 == 0:
  a_harf = a[h-1] + a[h]
  b_harf = b[h-1] + b[h]
  ans = b_harf - a_harf + 1
else:
  ans = b[h] - a[h] + 1
  
print(ans)
