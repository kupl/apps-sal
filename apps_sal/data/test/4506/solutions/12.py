n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [0] + a
b = [0] + b
# print(n, a, b)
for i in range(1, n + 1):
    a[i] *= i
    a[i] *= n + 1 - i
a.sort()
b.sort()
# print(n, a, b)
ans = 0
mod = 998244353
for i in range(1, 1 + n):
    ans += (a[i] * b[n + 1 - i]) % mod
    if ans >= mod:
        ans -= mod
print(ans)
