n, m = map(int, input().split())
t = [0] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    if t[a]:
        if t[a] == '1':
            t[b], t[c] = '2', '3'
        elif t[a] == '2':
            t[b], t[c] = '1', '3'
        else:
            t[b], t[c] = '1', '2'
    elif t[b]:
        if t[b] == '1':
            t[a], t[c] = '2', '3'
        elif t[b] == '2':
            t[a], t[c] = '1', '3'
        else:
            t[a], t[c] = '1', '2'
    elif t[c]:
        if t[c] == '1':
            t[a], t[b] = '2', '3'
        elif t[c] == '2':
            t[a], t[b] = '1', '3'
        else:
            t[a], t[b] = '1', '2'
    else:
        t[a], t[b], t[c] = '1', '2', '3'
print(' '.join(t[1:]))
