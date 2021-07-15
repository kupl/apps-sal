n, dest =  list(map(int, input().split()))
dest -= 1
a = list(map(int, input().split()))

m1 = float('inf'); m2 = float('inf')
pos1 = -1; pos2 = -1

for i in range(dest + 1):
    if a[i] <= m1:
        m1 = a[i]
        pos1 = i


for i in range(dest + 1, n):
    if a[i] <= m2:
        m2 = a[i]
        pos2 = i


if m2 < m1:
    c = 0
    for i in range(n):
        if dest + 1 <= i <= pos2:
            c += m2
            a[i] -= m2
        else:
            c += (m2+1)
            a[i] -= (m2+1)
    a[pos2] = c
else:
    c = 0
    for i in range(n):
        if pos1 + 1 <= i <= dest:
            c += m1 + 1
            a[i] -= m1 + 1
        else:
            c += m1
            a[i] -= m1
    a[pos1] = c
    
print(*a)

