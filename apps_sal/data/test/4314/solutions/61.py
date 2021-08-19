lst = input().split()
H = int(lst[0])
W = int(lst[1])


def update(S, n):
    return S[:n] + '*' + S[n + 1:]


field = []
for i in range(H):
    a = input()
    if a != '.' * W:
        field.append(a)
for i in range(W):
    t = 0
    for j in range(len(field)):
        if field[j][i] != '.':
            t = 1
            break
    if t == 0:
        for j in range(len(field)):
            field[j] = update(field[j], i)
for s in field:
    print(s.replace('*', ''))
