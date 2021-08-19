def pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(a, n // 2) ** 2 % 1000000007
    else:
        return a * pow(a, n // 2) ** 2 % 1000000007


M = 1000000007
(a, b, n, x) = map(int, input().split())
arr = [0] * 64
arr[0] = b
for i in range(1, 64):
    arr[i] = (pow(a, 2 ** (i - 1)) * arr[i - 1] % M + arr[i - 1]) % M
ans = pow(a, n) * x % M
pos = 0
for i in range(63, -1, -1):
    if 2 ** i <= n:
        ans += pow(a, pos) * arr[i] % M
        ans %= M
        n -= 2 ** i
        pos += 2 ** i
print(ans % M)
