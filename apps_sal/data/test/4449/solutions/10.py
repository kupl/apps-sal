def gns():
    return list(map(int, input().split()))


t = int(input())
for i in range(t):
    n = int(input())
    ns = gns()
    ns.sort()
    a = ns[0] * ns[-1]
    f = True
    for i in range(4 * n):
        if i % 2 == 1:
            continue
        if ns[i] != ns[i + 1]:
            f = False
            break
    if not f:
        print('NO')
        continue
    for i in range(4 * n):
        if ns[i] * ns[4 * n - 1 - i] != a:
            f = False
            break
    if not f:
        print('NO')
        continue
    print('YES')
