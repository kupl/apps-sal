n, k = map(int, input().split())

s = [0] * (k + 1)
ans = 0

for i in range(k, 0, -1):
    s[i] += pow(int(k / i), n, int(1e9 + 7))
    s[i] %= 1e9 + 7
    for j in range(i * 2, k + 1, i):
        s[i] += 1e9 + 7
        s[i] -= s[j]
        s[i] %= 1e9 + 7

for i in range(1, k+1):
    ans += i * s[i]
    ans %= 1e9 + 7

ans %= 1e9+7

print(int(ans))
