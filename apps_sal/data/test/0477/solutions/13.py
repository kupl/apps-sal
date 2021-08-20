bot = True
(n, m, i, j, a, b) = list(map(int, input().split()))
(x, y, t) = ([i - 1, n - i], [j - 1, m - j], [])
if all((i < a for i in x)) or all((j < b for j in y)):
    if 0 in x and 0 in y:
        t = [0]
else:
    u = [d // a for d in x if d % a == 0]
    v = [d // b for d in y if d % b == 0]
    t = [max(i, j) for i in u for j in v if (i + j) % 2 == 0]
print(min(t) if t else 'Poor Inna and pony!')
