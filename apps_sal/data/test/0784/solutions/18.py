(q, w) = map(int, input().split())
a = []
while w > q:
    if w % 10 == 1:
        a.append(w)
        w //= 10
    elif w % 2 == 1:
        w = q - 1
    else:
        a.append(w)
        w //= 2
a.append(w)
if w == q:
    print('YES')
    print(len(a))
    for i in a[::-1]:
        print(i, end=' ')
else:
    print('NO')
