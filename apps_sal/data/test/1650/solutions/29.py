l = list(input())
n = len(l)
mod = pow(10, 9) + 7
m = pow(10, 5) + 5
p2 = [1] * m
p3 = [1] * m
for i in range(1, m):
    p2[i] = (p2[i - 1] * 2) % mod
    p3[i] = (p3[i - 1] * 3) % mod
cnt = 0
ans = 0
for i in range(n):
    if l[i] == "1":
        ans += ((p3[n - i - 1] * p2[cnt]) % mod)
        ans %= mod
        cnt += 1
ans += p2[cnt]
ans %= mod
print(ans)
