#import math
#import collections
n,k = map(int, input().split( ))
A = list(map(int, input().split( )))

arr = [0]*n
for i in range(n):
  arr[i] = (A[i]+1)/2

s = sum(arr[:k])
ans = s
for j in range(n-k):
  s = s - arr[j] + arr[j+k]
  ans = max(s,ans)
print(ans)
