__author__ = 'zhan'
[a1, b1] = [int(i) for i in input().split()]
[a2, b2] = [int(i) for i in input().split()]
q = [[[a1, b1, 0]], [[a2, b2, 0]]]
total = [0, 0]
tested = [[], []]


def expand(i):
    if not q[i][0][0] & 1:
        tt = [q[i][0][0] // 2, q[i][0][1], q[i][0][2] + 1]
        if not tt[0] * tt[1] in tested[i]:
            q[i].append(tt)
            tested[i].append(tt[0] * tt[1])
    if q[i][0][0] % 3 == 0:
        tt = [q[i][0][0] // 3 * 2, q[i][0][1], q[i][0][2] + 1]
        if not tt[0] * tt[1] in tested[i]:
            q[i].append(tt)
            tested[i].append(tt[0] * tt[1])
    if not q[i][0][1] & 1:
        tt = [q[i][0][0], q[i][0][1] // 2, q[i][0][2] + 1]
        if not tt[0] * tt[1] in tested[i]:
            q[i].append(tt)
            tested[i].append(tt[0] * tt[1])
    if q[i][0][1] % 3 == 0:
        tt = [q[i][0][0], q[i][0][1] // 3 * 2, q[i][0][2] + 1]
        if not tt[0] * tt[1] in tested[i]:
            q[i].append(tt)
            tested[i].append(tt[0] * tt[1])
    q[i].pop(0)
    q[i].sort(key=lambda x: x[0] * x[1], reverse=True)


while True:
    if len(q[0]) > 0 and len(q[1]) > 0:
        total[0] = q[0][0][0] * q[0][0][1]
        total[1] = q[1][0][0] * q[1][0][1]
        if total[0] > total[1]:
            expand(0)
        elif total[0] < total[1]:
            expand(1)
        else:
            print(str(q[0][0][2] + q[1][0][2]) + '\n' + str(q[0][0][0]) + ' ' + str(q[0][0][1]) + '\n' + str(q[1][0][0]) + ' ' + str(q[1][0][1]))
            break
    else:
        print(-1)
        break
