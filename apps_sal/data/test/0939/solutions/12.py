(n, m) = map(int, input().split())
t = [0] * (n + 1)
for j in range(m):
    (a, b, c) = map(int, input().split())
    x = t[a] | t[b] | t[c]
    for i in (a, b, c):
        if not t[i]:
            if not x & 1:
                t[i] = 1
                x += 1
            elif not x & 2:
                t[i] = 2
                x += 2
            else:
                t[i] = 4
p = {0: '1 ', 1: '1 ', 2: '2 ', 4: '3 '}
print(''.join((p[i] for i in t[1:])))
