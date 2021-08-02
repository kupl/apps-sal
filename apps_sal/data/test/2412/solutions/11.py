q = int(input())
for _ in range(q):
    n = int(input())
    u = list(map(int, list(input())))
    k = -1
    for i in range(n):
        if u[i] == 8:
            k = i
            break
    if k == -1:
        print('NO')
        continue
    if n - k >= 11:
        print('YES')
    else:
        print('NO')
