m, s = input().split()
m, s = int(m), int(s)
if 9 * m < s or (s == 0 and m != 1):
    print(-1, -1)
else:
    lis = [0 for i in range(m)]
    q = int(s // 9)
    r = int(s % 9)
    if s == 0:
        print(0, 0)
    elif m == 1 and s == 9:
        print(9, 9)
    elif m == 2 and s == 18:
        print(99, 99)
    elif q == m - 1:
        for i in range(q):
            lis[i] = '9'
        lis[m - 1] = str(r)
        lis1 = lis[:]
        if r != 0:
            print(int(''.join(lis[::-1])), int(''.join(lis)))
        else:
            print(int(''.join(['1', '8'] + lis[::-1][2:m])), int(''.join(lis1)))
    elif q < m - 1:
        for i in range(q):
            lis[i] = '9'
        lis[q] = str(r)
        for i in range(q + 1, m):
            lis[i] = '0'
        lis1 = lis[:]
        if r != 0:
            lis[m - 1] = '1'
            lis[q] = str(r - 1)
            print(int(''.join(lis[::-1])), int(''.join(lis1)))
        else:
            lis[m - 1] = '1'
            lis[q - 1] = '8'
            print(int(''.join(lis[::-1])), int(''.join(lis1)))
    else:
        for i in range(m):
            lis[i] = '9'
        print(int(''.join(lis)), int(''.join(lis)))
