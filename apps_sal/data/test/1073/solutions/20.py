n = int(input())
l = input()
v = []
h = []
for c in l:
    if c == 'U':
        v += [1]
    elif c == 'D':
        v += [-1]
    else:
        v += [0]
    if c == 'R':
        h += [1]
    elif c == 'L':
        h += [-1]
    else:
        h += [0]
for i in range(1, n):
    v[i] += v[i - 1]
    h[i] += h[i - 1]
v = [0] + v
h = [0] + h
a = 0
for i in range(n):
    for j in range(i, n):
        if h[j + 1] == h[i] and v[j + 1] == v[i]:
            a += 1
print(a)
