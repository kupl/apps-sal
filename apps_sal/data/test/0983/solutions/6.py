n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
max_pa_i = [0] * n
max_pa_i[0] = a[0] * p
for i in range(1, n):
    max_pa_i[i] = max(a[i] * p, max_pa_i[i - 1])
max_ra_k = [0] * n
max_ra_k[-1] = a[-1] * r
for i in range(n - 2, -1, -1):
    max_ra_k[i] = max(a[i] * r, max_ra_k[i + 1])
x = -10 ** 19
for i in range(n):
    x = max(x, max_pa_i[i] + q * a[i] + max_ra_k[i])
print(x)
