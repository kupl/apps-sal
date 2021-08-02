n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
ans = 0
for i in range(n):
    sum += a[i]
for i in range(n):
    if a[i] >= sum / (4 * m):
        ans += 1
if ans >= m:
    print("Yes")
else:
    print("No")
