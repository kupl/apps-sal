mod = 10**9 + 7
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
ans = 0
total = pow(2, 2 * n - 2, mod)
for i in range(n):
    ans += total * (n - i + 1) * arr[i]
    ans %= mod
print((int(ans)))
