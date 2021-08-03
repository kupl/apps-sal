def best(h, n, x):
    best = ''
    bestCnt = 10
    begin = 0
    end = n
    if x == 'h':
        if n == 12:
            begin = 1
            end = 13
    for i in range(begin, end):
        si = str(i)
        if len(si) == 1:
            si = '0' + si
        bad = 0
        for x, y in zip(h, si):
            if x != y:
                bad += 1
        if bad < bestCnt:
            bestCnt = bad
            best = si
    return best


n = int(input())
s = input()
h = s[0:2]
m = s[3:5]
print(best(h, n, 'h'), best(m, 60, 'm'), sep=':')
