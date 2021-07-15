n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d, i, t = 0, 0, 0
while i < m:
    pg = (a[i] - d - 1)//k
    j = i
    while j < m and (a[j] - d - 1)//k == pg:
        j += 1
    d += j - i
    t += 1
    i = j
print(t)

