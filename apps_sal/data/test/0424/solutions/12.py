n = int(input())
ans = n
f = [0] * (n + 1)
for i in range(2, n + 1):
    if f[i] == 0:
        for j in range(i * 2, n + 1, i):
            f[j] = i
    f[i] = i - f[i] + 1
for i in range(f[n], n + 1):
    ans = min(ans, f[i])
print(ans)
