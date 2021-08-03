n = int(input())
a = list(map(int, input().split()))
ans = 0
m = 1
for i in range(n):
    if a[i] == m:
        m += 1
    else:
        ans += 1
if ans == n:
    ans = -1

print(ans)
