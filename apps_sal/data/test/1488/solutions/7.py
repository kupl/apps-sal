def gcd(m, n): return m if n == 0 else gcd(n, m % n)


n = int(input())

a = sorted(map(int, input().split()))

cur = sum(a)
ans = cur
pre = 0

for i in range(n):
    cur += (i + i - n) * (a[i] - pre)
    ans += cur
    pre = a[i]

g = gcd(ans, n)

print(ans // g, n // g)
