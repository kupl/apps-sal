(n, k) = list(map(int, input().split()))
cnt = {}
for i in range(2 ** k):
    cnt[bin(i)[2:].zfill(k)] = 0
for i in range(n):
    l = input().split()
    s = ''
    for x in l:
        s += x
    cnt[s] += 1


def f1():
    if cnt['0'] > 0:
        print('YES')
    else:
        print('NO')


def f2():
    if cnt['00'] > 0:
        print('YES')
        return
    if cnt['01'] > 0 and cnt['10'] > 0:
        print('YES')
        return
    print('NO')


def f3():
    if cnt['000'] > 0:
        print('YES')
        return
    a = int(cnt['100'] > 0)
    b = int(cnt['010'] > 0)
    c = int(cnt['001'] > 0)
    if a + b + c > 1:
        print('YES')
        return
    if a and cnt['011']:
        print('YES')
        return
    if b and cnt['101']:
        print('YES')
        return
    if c and cnt['110']:
        print('YES')
        return
    print('NO')


def f4():
    if cnt['0000'] > 0:
        print('YES')
        return
    ms = ['0001', '1110', '0010', '1101', '0100', '1011', '1000', '0111', '1100', '0011', '1010', '0101', '1001', '0110']
    for i in range(len(ms) // 2):
        if cnt[ms[2 * i]] > 0 and cnt[ms[2 * i + 1]] > 0:
            print('YES')
            return
    x = 0
    for i in range(4):
        if cnt[ms[i * 2]] > 0:
            x += 1
    if x > 1:
        print('YES')
        return
    ind = []
    if cnt['0001'] > 0:
        ind.append(3)
    if cnt['0010'] > 0:
        ind.append(2)
    if cnt['0100'] > 0:
        ind.append(1)
    if cnt['1000'] > 0:
        ind.append(0)
    for i in range(len(ms)):
        b = False
        for x in ind:
            if ms[i][x] == '0':
                b = True
        if not b:
            continue
        if cnt[ms[i]] > 0:
            print('YES')
            return
    print('NO')
    return


[f1, f2, f3, f4][k - 1]()
