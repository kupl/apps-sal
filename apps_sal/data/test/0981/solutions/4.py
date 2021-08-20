def f(t, k, d):
    j = k - 1
    for i in range(k, 9):
        if d >= t[i]:
            j = i
    return (d - t[j], j + 1)


n = int(input())
t = list(map(int, input().split()))
(m, k) = (t[0], 1)
for (i, x) in enumerate(t, 1):
    if x <= m:
        (m, k) = (x, i)
if n < m:
    print(-1)
else:
    (d, j, s) = (n % m, k + 1, [])
    while j != k:
        (d, j) = f(t, k, d + m)
        s.append(j)
    print(''.join(map(str, s)) + str(k) * (n // m - len(s)))
