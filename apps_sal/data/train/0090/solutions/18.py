t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = []
    for i in range(n):
        if b[i] == 0:
            c.append(a[i])
    c.sort(reverse=True)
    k = 0
    for i in range(n):
        if b[i] == 0:
            a[i] = c[k]
            k += 1
    print(' '.join((str(j) for j in a)))
