n = int(input())
a = list(map(int, input().split()))
now = 1
ans = 0
for i in range(n):
    if a[i] != now:
        ans += 1
    else:
        now += 1
if now == 1:
    print(-1)
else:
    print(ans)
