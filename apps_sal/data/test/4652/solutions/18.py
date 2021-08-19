q = int(input())
for i in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    q = p + p + p
    p = sorted(p)
    r = p[::-1]
    f = 0
    for k in range(2 * n):
        if q[k:k + n] == r or q[k:k + n] == p:
            f = 1
            break
    if f == 0:
        print('NO')
    else:
        print('YES')
