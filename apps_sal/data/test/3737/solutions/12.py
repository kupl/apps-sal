import sys
n = int(input())
a = list(map(int, input().split()))
mn = min(a)
mx = max(a)
ans = 0
for i in range(n):
    if a[i] > mn and a[i] < mx:
        ans += 1
print(ans)
