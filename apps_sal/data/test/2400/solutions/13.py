import sys
t = int(sys.stdin.readline())
ans_arr = []
for w in range(t):
    n = int(sys.stdin.readline())
    p = [int(i) for i in sys.stdin.readline().split()]
    m = int(sys.stdin.readline())
    q = [int(i) for i in sys.stdin.readline().split()]
    peven = 0
    podd = 0
    for e in range(n):
        if p[e] % 2 == 0:
            peven += 1
        else:
            podd += 1
    qeven = 0
    qodd = 0
    for f in range(m):
        if q[f] % 2 == 0:
            qeven += 1
        else:
            qodd += 1
    ans_arr.append(str(podd * qodd + peven * qeven))
print('\n'.join(ans_arr))
