import math

n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
a.append(math.inf)
for i in range(n):
    ans += min(t, a[i + 1] - a[i])
print(ans)

