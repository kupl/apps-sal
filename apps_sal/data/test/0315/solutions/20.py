(n, k) = (int(i) for i in input().split())
l = [int(i) for i in input().split()]
c = 0
for i in range(1, n):
    if l[i - 1] + l[i] < k:
        a = k - (l[i - 1] + l[i])
        c += a
        l[i] += a
print(c)
print(' '.join((str(i) for i in l)))
