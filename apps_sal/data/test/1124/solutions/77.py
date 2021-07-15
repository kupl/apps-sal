N = int(input())
a = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    elif m > n:
        return gcd(m, n)
    return gcd(m, n % m)

if N == 1:
    print(a[0])
else:
    ans = gcd(a[0], a[1])
    for i in range(2, N):
        ans = gcd(ans, a[i])
    print(ans)
