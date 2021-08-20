n = int(input())
u = list(map(int, input().split()))
u = sorted(u)
ans = 0
for i in range(n - 1):
    if ans == 0:
        ans = (u[i] + u[i + 1]) / 2
    else:
        ans = (ans + u[i + 1]) / 2
print(ans)
