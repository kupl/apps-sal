n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
mod = 10 ** 9 + 7
ans = 0
for i in range(n - 1, -1, -1):
    ans += (2 + i) * l[i]
b = pow(2, 2 * n - 2, mod)
print(ans * b % mod)
