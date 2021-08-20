(n, m) = map(int, input().split())
f = list(map(int, input().split()))
b = list(map(int, input().split()))
f_back = dict()
keys = set()
for i in range(n):
    if f[i] in keys:
        f_back[f[i]] = -1
    else:
        f_back[f[i]] = i
        keys.add(f[i])
state = 1
a = [0] * m
for i in range(m):
    if b[i] in keys:
        if state == 1:
            if f_back[b[i]] == -1:
                state = 2
            else:
                a[i] = f_back[b[i]] + 1
    else:
        state = 0
        break
if state == 1:
    print('Possible')
    print(' '.join(map(str, a)))
elif state == 2:
    print('Ambiguity')
else:
    print('Impossible')
