import sys
n = int(input())
a = [int(tmp) for tmp in input().split()]
ans = 0
now = 0
for i in range(n):
    ans += abs(a[i] - now)
    now += a[i] - now
print(ans)
