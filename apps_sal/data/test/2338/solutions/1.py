def f(i, j):
    x, y = str(abs(i)), str(abs(j))
    l, r, u, d = ' L', ' R', ' U', ' D'
    if i < 0: l, r = r, l
    if j < 0: u, d = d, u
    if i:
        if j: return ['1 ' + x + r, '1 ' + y + u, '2', '1 ' + x + l, '1 ' + y + d, '3']
        else: return ['1 ' + x + r, '2', '1 ' + x + l, '3']
    else: return ['1 ' + y + u, '2', '1 ' + y + d, '3']

p, n = [], int(input())
t = [(abs(i) + abs(j), i, j) for i, j in tuple(map(int, input().split()) for i in range(n))]
t.sort()
for r, i, j in t:
    p += f(i, j)
print(len(p))
print('\n'.join(p))
