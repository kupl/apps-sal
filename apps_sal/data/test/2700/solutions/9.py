
T = int(input())
l = []
for i in range(T):
    l += [[int(j) for j in input().split()]]

l1 = []
for i in l:
    a, b, c, d = tuple(i)
    if a >= d:
        l1 += [0]

    elif b < c:
        l1 += [(b - a + 1) * (d - c + 1)]

    elif c <= a <= d <= b:
        n = d - a
        l1 += [n * (n + 1) / 2]

    elif c <= a <= b <= d:
        l1 += [(d - a) * (d - a + 1) / 2
               - (d - b - 1) * (d - b) / 2]

    elif a < c <= d <= b:
        l1 += [(d - c + 1) * (c - a)
               + (d - c) * (d - c + 1) / 2]

    elif a < c <= b <= d:
        l1 += [(d - c + 1) * (c - a)
               + (d - c) * (d - c + 1) / 2
               - (d - b - 1) * (d - b) / 2]

    else:
        l1 += [0]

for i in l1:
    print(i)
