n = int(input())
A = list(map(int, input().split()))
m = 1
ans = 0
for a in A:
    if a == m:
        m += 1
    else:
        ans += 1
if ans < n:
    print(ans)
else:
    print(-1)
