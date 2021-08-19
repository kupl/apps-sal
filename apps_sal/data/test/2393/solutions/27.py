k = int(input())


def pandora(v):
    if len(v) < 3:
        print(0)
        return
    if len(v) == 3:
        if v[0] == 'o' and v[1] == 'n' and (v[2] == 'e') or (v[0] == 't' and v[1] == 'w' and (v[2] == 'o')):
            print('1\n1')
            return
    q = 0
    z = []
    v.append('h')
    for i in range(3, len(v)):
        if v[i - 3] == 'o' and v[i - 2] == 'n' and (v[i - 1] == 'e'):
            q += 1
            z.append(i - 2 + 1)
        if v[i - 3] == 't' and v[i - 2] == 'w' and (v[i - 1] == 'o'):
            if v[i] == 'o':
                q += 1
                z.append(i - 2 + 1)
            else:
                q += 1
                z.append(i - 1 + 1)
                v[i - 1] = 'q'
    print(q)
    print(' '.join(list([str(x) for x in z])))


for _ in range(k):
    pandora(list(input()))
