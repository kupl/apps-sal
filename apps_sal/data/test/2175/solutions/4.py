n = int(input())
a = [int(i) for i in input().split()]
b = [0] * n
after = list(map(int, list(range(1, n + 2))))


def add_water(p, x):
    i = p - 1
    skip = []
    while x > 0 and i < n:
        space = a[i] - b[i]
        if x >= space:
            x -= space
            b[i] = a[i]
            skip.append(i)
            i = after[i]
        else:
            b[i] += x
            break
    for j in skip:
        after[j] = i


m = int(input())
P = []
for i in range(m):
    l = [int(j) for j in input().split()]
    if l[0] == 1:
        add_water(l[1], l[2])
    else:
        P.append(b[l[1] - 1])
for j in P:
    print(j)
