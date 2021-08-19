for t in range(int(input())):
    (n, s) = input().split()
    s = int(s)
    nn = ['0', '0', '0'] + list(n)
    su = 0
    for i in n:
        su += int(i)
    ptr = 1
    while su > s:
        su -= int(nn[-ptr])
        su += 1
        nn[-ptr] = '0'
        nn[-ptr - 1] = str(1 + int(nn[-ptr - 1]))
        itr = 1
        while int(nn[-ptr - itr]) >= 10:
            su -= 10
            su += int(nn[-ptr - itr]) // 10
            nn[-ptr - itr - 1] = str(int(nn[-ptr - itr - 1]) + int(nn[-ptr - itr]) // 10)
            nn[-ptr - itr] = str(int(nn[-ptr - 1]) % 10)
            itr += 1
        ptr += 1
    print(int(''.join(nn)) - int(n))
