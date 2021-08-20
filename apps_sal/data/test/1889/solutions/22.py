def func(a):
    ans = 0
    an = 0
    for i in a:
        if i == 0:
            ans = max(ans, an)
            an = 0
        else:
            an += 1
    return max(ans, an)


(n, m, q) = (int(x) for x in input().split(' '))
a = [[int(x) for x in input().split()] for i in range(n)]
mas = [func(a[i]) for i in range(n)]
for _ in range(q):
    (x, y) = (int(i) - 1 for i in input().split(' '))
    a[x][y] = 1 if a[x][y] == 0 else 0
    mas[x] = func(a[x])
    print(max(mas))
