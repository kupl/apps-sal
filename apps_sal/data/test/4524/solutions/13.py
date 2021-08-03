n, m = [int(s) for s in input().split()]
a = input()
b = input()
ones = 0
ans = 0
for i in range(m):
    if b[i] == '1':
        ones += 1
    if n >= m - i:
        ans <<= 1
        ans %= 998244353
        if a[n - (m - i)] == '1':
            ans += ones
            ans %= 998244353

print(ans)
