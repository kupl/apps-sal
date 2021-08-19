(n, m) = map(int, input().split())
dancers = {'auther': 'wanglizhi'}
for i in range(m):
    (a, b, c) = map(int, input().split())
    if a in dancers:
        color = dancers[a]
        dancers[b] = (color + 1) % 3
        dancers[c] = (color + 2) % 3
    elif b in dancers:
        color = dancers[b]
        dancers[a] = (color + 1) % 3
        dancers[c] = (color + 2) % 3
    elif c in dancers:
        color = dancers[c]
        dancers[a] = (color + 1) % 3
        dancers[b] = (color + 2) % 3
    else:
        dancers[a] = 0
        dancers[b] = 1
        dancers[c] = 2
for i in range(n - 1):
    print(dancers[i + 1] + 1, end=' ')
print(dancers[n] + 1)
