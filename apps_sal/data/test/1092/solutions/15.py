M = 1000000007
f = [1] * 2000
for i in range(1, 2000):
    f[i] = f[i - 1] * i % M
n, m = list(map(int, input().split()))
a = sorted(map(int, input().split()))
b = []
for i in range(1, m):
    x = a[i] - a[i - 1] - 1
    if(x > 0):
        b.append(x)
count = pow(2, sum(b) - len(b), M) * f[n - m] % M
b = [a[0] - 1] + b + [n - a[-1]]
for i in b:
    count = count * pow(f[i], M - 2, M) % M
print(count)
