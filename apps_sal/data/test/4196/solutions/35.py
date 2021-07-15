#a, b, k = map(int, input().split( ))
import math

 
n = int(input())
a = list(map(int,input().split()))

left = [0] * (n + 1)
right = [0] * (n + 1)
for i in range(n):
    left[i + 1] = (math.gcd(left[i],a[i]))
    right[n - i - 1] = (math.gcd(right[n - i],a[n - 1 - i]))
#print(left, right)

ans = 0
for i in range(n):
  ans = max(ans, math.gcd(left[i],right[i+1]))
print(ans)
