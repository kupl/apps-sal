import sys
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dif = []
for i in range(n):
    dif.append((a[i] - b[i], a[i], b[i]))
dif.sort()
ans = 0
for i in range(0, k):
    ans += dif[i][1]

for i in range(k, n):
    ans += min(dif[i][1], dif[i][2])
print(ans)
