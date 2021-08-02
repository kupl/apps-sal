n = int(input())
z = list(map(int, input().split()))
for i in range(n):
    z[i] = [z[i], i]
z.sort()
ans = 1e9
for i in range(1, n):
    if z[i][0] == z[0][0]:
        ans = min(ans, z[i][1] - z[i - 1][1])
print(ans)
