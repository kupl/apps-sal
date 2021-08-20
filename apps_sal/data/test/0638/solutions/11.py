(n, m) = map(int, input().split())
a = [int(i) for i in input().split()]
for i in range(n):
    c = m - a[i]
    b = sorted(a[:i], reverse=True)
    s = sum(b)
    j = 0
    while s > c:
        s -= b[j]
        j += 1
    print(j, end=' ')
