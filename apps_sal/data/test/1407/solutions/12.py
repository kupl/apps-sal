def sieve(mx):
    a = [0] * (mx + 1)
    a[0] = a[1] = 1
    for (i, e) in enumerate(a):
        if e == 0:
            for n in range(i * i, mx + 1, i):
                a[n] = 1
    return a


p = sieve(10 ** 5 + 100)
for i in range(10 ** 5 + 99, 0, -1):
    p[i] *= p[i + 1] + 1
(n, m) = map(int, input().split())
cols = [0] * m
mm = 10 ** 7
for i in range(n):
    row = list(map(int, input().split()))
    row_sum = 0
    for (a, j) in enumerate(row):
        tt = p[j]
        row_sum += tt
        cols[a] += tt
    mm = min(mm, row_sum)
print(min(min(cols), mm))
