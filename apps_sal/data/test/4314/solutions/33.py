(h, w) = list(map(int, input().split()))
a = []
for i in range(h):
    s = input()
    if s.count('#') > 0:
        a.append(s)
b = [0 for i in range(w)]
for gl in a:
    for i in range(w):
        if gl[i] == '#':
            b[i] += 1
for gl in a:
    v = ''
    for i in range(w):
        if b[i] > 0:
            v += gl[i]
    print(v)
