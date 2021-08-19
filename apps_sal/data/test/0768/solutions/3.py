(n, m, t) = map(int, input().split())
a = []
for kitten in range(n):
    a.append(input())
c = 0
for i in range(m):
    l = 0
    for j in range(n):
        if a[j][i] == 'Y':
            l += 1
    if l >= t:
        c += 1
print(c)
