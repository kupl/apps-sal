n = int(input())
a = [int(c == 'b') for c in input()]
b = [int(c == 'b') for c in input()]
x = [i + 1 for i in range(n) if (a[i], b[i]) == (0, 1)]
y = [i + 1 for i in range(n) if (a[i], b[i]) == (1, 0)]
if (len(x) & 1) ^ (len(y) & 1) == 1:
    print(-1)
    return
cnt = 0
res = []
while len(x) > 1:
    res.append(f'{x.pop()} {x.pop()}')
    cnt += 1
while len(y) > 1:
    res.append(f'{y.pop()} {y.pop()}')
    cnt += 1
if len(x) == 1:
    c, d = x[0], y[0]
    res.append(f'{c} {c}')
    res.append(f'{c} {d}')
    cnt += 2
print(cnt)
print('\n'.join(res))
