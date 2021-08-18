def print_pattern(n):
    a = [1]
    b = []
    c = []
    d = []
    for i in range(n):
        if i != 0:
            a.append((a[i - 1] + 1) * 2)
    for i in range(n):
        b.append(a[i] + 1)
    for i in range(n - 1):
        c.append(a[i + 1])
    c.append((a[n - 1] + 1) * 2)
    for i in range(n):
        d.append(a[i] + 2)
    for i in range(n):
        print(a[i], end=" ")
    print()
    for i in range(n):
        print(b[i], end=" ")
    print()
    for i in range(n):
        print(c[i], end=" ")
    print()
    for i in range(n):
        print(d[i], end=" ")
    print()
    return


t = int(input())
n = [int(x) for x in input().split()]
for i in n:
    m = print_pattern(int(i))
