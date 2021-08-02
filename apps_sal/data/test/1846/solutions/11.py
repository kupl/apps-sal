with open('input.txt', 'r') as g:
    n = int(g.readline())
    lst = list(map(int, g.readline().split()))
    x, y = 0, 0
    for i, e in enumerate(lst):
        if e <= 0:
            y += 1
    mn = 10**9
    for i in range(1, n):
        if lst[i - 1] > 0:
            x += 1
        if lst[i - 1] < 0:
            y -= 1
        if x + y < mn:
            mn = x + y
with open('output.txt', 'w') as d:
    d.write(str(mn))
