sb = input().split()
s = int(sb[0])
b = int(sb[1])
a = list(map(int, input().split()))
bases = []


for _ in range(b):
    dg = list(map(int, input().split()))
    bases.append(dg)

bases.sort(key=lambda a: a[0])

sum_total = 0
for i in bases:
    sum_total += i[1]
    i[1] = sum_total

dg = [*zip(*bases)]

a_sorted = []
a_sorted += a
a_sorted.sort()
g = []
j = 0
for i in a_sorted:
    while j < b:
        if dg[0][j] > i:
            if j > 0:
                g.append(dg[1][j - 1])
            else:
                g.append(0)
            break
        elif j == b - 1:
            g.append(dg[1][j])
            break
        j += 1


for i in a:
    index = a_sorted.index(i)
    print(g[index], end=' ')
