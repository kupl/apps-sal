import sys
T = int(sys.stdin.readline().strip())


def getT(line):
    return map(int, line.strip().split(' '))


for t in range(T):
    (m, n) = getT(sys.stdin.readline())
    if min(m, n) == 1:
        print('YES')
    elif min(m, n) == 2 and max(m, n) == 2:
        print('YES')
    else:
        print('NO')
