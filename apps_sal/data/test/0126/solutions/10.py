n = int(input())
L = [int(x) for x in input()]
C = [None] * 10
p = {}
for i in range(1, 10):
    C[i] = ((i - 1) // 3, (i - 1) % 3)
    p[C[i]] = True
C[0] = (3, 1)
p[C[0]] = True
cnt = 0
possib = []
q = [(i, j) for i in range(-6, 7) for j in range(-6, 7)]
for base in q:
    gone = False
    for num in L:
        diff = C[num]
        nn = (diff[0] + base[0], diff[1] + base[1])
        if nn not in p:
            gone = True
            break
    if not gone:
        possib.append(base)
        cnt += 1
if cnt == 1:
    print('YES')
else:
    print('NO')
