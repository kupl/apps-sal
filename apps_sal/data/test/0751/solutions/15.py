(n, m), a, b, c = list(map(int, input().split())), list(map(int, input().split())), 0, 0

a.append(m + 1)

for i in range(len(a) - 1):
    if b + a[i] <= m and b + a[i] + a[i + 1] > m:
        b = 0
        c = c + 1
    else:
        b = b + a[i]

print(c)
