mod = 1000000007
n, m = list(map(int, input().split()))
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

xc = 0
for i in range(1, n):
    a = x[i] - x[i - 1]
    l = min(i, n - i)
    # xc+=a*(l*n-((l*l+l)//2))
    xc += a * (l * (n - l))
    xc %= mod

yc = 0
for i in range(1, m):
    a = y[i] - y[i - 1]
    l = min(i, m - i)
    # yc+=a*(l*m-((l*l+l)//2))
    yc += a * (l * (m - l))
    yc %= mod
print(((xc * yc) % mod))
