k = int(input())
q = input()


def program(k, q):
    if k > len(set(q)):
        print('NO')
        return
    used = []
    ss = []
    while len(q) > 0:
        ch = q[0]
        q = q[1:]
        if ch in used or k - len(ss) == 0:
            ss[-1] += ch
        else:
            ss.append(ch)
        used.append(ch)
    print('YES')
    for s in ss:
        print(s)


program(k, q)
