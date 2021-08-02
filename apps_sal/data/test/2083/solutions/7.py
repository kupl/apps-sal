n, t, c = input().split()
n = int(n)
t = int(t)
c = float(c)
a = list(map(int, input().split()))
m = int(input())
p = list(map(int, input().split()))
sums = [a[0]]
for i in range(1, n):
    sums.append(sums[i - 1] + a[i])
approx = [a[0] / (t * c)]
for i in range(1, n):
    approx.append((approx[i - 1] + a[i] / t) / c)

for i in range(m):
    real = (sums[p[i] - 1] - (0 if p[i] == t else sums[p[i] - t - 1])) / t
    appr = (approx[p[i] - 1])  # - (0 if p[i] == t else approx[p[i] - t - 1] / (c ** t)))
    print(real, appr, abs(real - appr) / real)
