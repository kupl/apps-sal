s = input()
n = len(s)

c = [0]
tmp = 'R'
idx = 0
for i in s:
    if tmp == i:
        c[idx] += 1
    else:
        tmp = i
        idx += 1
        c.append(1)


for i in range(0, len(c), 2):
    r, l = c[i], c[i + 1]
    rl = r + l
    for j in range(r - 1):
        print(0, end=' ')
    if not rl % 2:
        print(rl // 2, rl // 2, end=' ')
    elif not r % 2:
        print(rl // 2, rl // 2 + 1, end=' ')
    else:
        print(rl // 2 + 1, rl // 2, end=' ')
    for j in range(l - 1):
        print(0, end=' ')
