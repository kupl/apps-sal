n = int(input())
u = list(map(int, list(input())))
ans = 0
for i in range(n):
    if u[i] % 2 == 0:
        ans += i + 1
print(ans)

