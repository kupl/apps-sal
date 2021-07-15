import math

n = int(input())
a = list(map(int, input().split()))
s = sum(a)
a.sort()
ans = s
for i in range(n - 1, 0, -1):
    cur = s - a[0] - a[i]
    for j in range(2, int(math.sqrt(a[i]) + 1)):
        if a[i] % j == 0:
            ans = min(ans, cur + a[0] * j + a[i] // j)
print(ans)

