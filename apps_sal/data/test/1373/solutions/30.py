n, k = map(int, input().split())

MOD = 10 ** 9 + 7

H = 0
L = 0
for i in range(k):
    L += i
    H += (n - i)

ans = 0
a = k
b = n - k
for i in range(n + 2 - k):
    ans += H - L + 1
    L += a
    H += b
    a += 1
    b -= 1
    ans %= MOD

print(ans)
