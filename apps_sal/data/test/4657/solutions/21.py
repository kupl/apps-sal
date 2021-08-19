import time
import sys
start = time.time()
q = int(sys.stdin.readline().rstrip())
for i in range(0, q):
    ns = [int(j) for j in sys.stdin.readline().rstrip().split(' ')]
    n = ns[0]
    k = ns[1]
    ln = [int(j) for j in sys.stdin.readline().rstrip().split(' ')]
    if len(ln) == 1:
        if ln[0] % 2 == 1:
            print('YES')
            print(1)
        else:
            print('NO')
        continue
    cc = 1
    inc = 0
    inds = []
    for j in range(0, len(ln)):
        if ln[j] % 2 == 1:
            if inc < k - 1:
                inc += 1
                inds.append(j + 1)
            elif inc < k:
                inc += 1
            else:
                cc += 1
    if inc < k or cc % 2 == 0:
        print('NO')
    else:
        inds.append(n)
        print('YES')
        print(' '.join([str(j) for j in inds]))
