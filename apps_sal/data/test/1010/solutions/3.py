n = int(input())
a = list(map(int, input().split()))
ans = 1
i = 0
while i < n and a[i] != 1:
    i += 1
if i == n:
    ans = 0
cur = 1
for j in range(i + 1, n):
    if a[j] == 1:
        ans *= cur
        cur = 1
    else:
        cur += 1
print(ans)
