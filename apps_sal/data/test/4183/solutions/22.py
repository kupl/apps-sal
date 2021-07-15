def lcm(m, n):
    return m//gcd(m, n)*n


def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n


n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 1
for i in arr:
    ans = lcm(ans, i)

print(ans)
