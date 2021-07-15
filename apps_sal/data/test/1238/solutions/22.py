n = int(input())
u = list(map(int, input().split()))
u.sort()
ans = 0
for i in range(1, n):
    ans += u[i] - u[i - 1] - 1
print(ans)

