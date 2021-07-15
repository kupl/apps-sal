n = int(input())
u = list(map(int, input().split()))
u.sort()
ans = 0
for i in range(n):
    if ans < u[i]:
        #5print(ans, u[i])
        ans += 1
print(ans)

