n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
u = [0] * (n + 1)
for i in range(n):
    if u[i] == 0:
        ans += 1
    for j in range(i, n):
        if a[j] % a[i] == 0:
            u[j] = 1
print(ans)
