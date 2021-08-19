def first():
    inp = input().split(' ')
    n = int(inp[0])
    c = int(inp[1])
    p = []
    t = []
    ip = input().split(' ')
    for i in ip:
        p.append(int(i))
    it = input().split(' ')
    for i in it:
        t.append(int(i))
    (fs, ft) = (0, 0)
    (ss, st) = (0, 0)
    for i in range(n):
        ft += t[i]
        fs += max(0, p[i] - c * ft)
        st += t[n - i - 1]
        ss += max(0, p[n - i - 1] - c * st)
    if fs > ss:
        print('Limak')
    elif ss > fs:
        print('Radewoosh')
    else:
        print('Tie')


first()
