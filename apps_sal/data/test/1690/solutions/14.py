n = int(input())
u = list(map(int, input().split()))
for i in range(n - 2, -1, -1):
    if u[i] >= u[i + 1] and u[i] != 0:
        u[i] = u[i + 1] - 1
        if u[i + 1] == 0:
            u[i] = 0
print(sum(u))
