n = int(input())
(x, y) = (0, 0)
t = 0
for i in range(n):
    (ti, xi, yi) = list(map(int, input().split()))
    l = abs(xi - x + yi - y)
    if l <= ti - t and l % 2 == (ti - t) % 2:
        (x, y) = (xi, yi)
        t = ti
    else:
        print('No')
        break
else:
    print('Yes')
