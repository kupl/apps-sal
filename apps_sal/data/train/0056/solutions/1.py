q = int(input())
for _ in range(q):
    (n, k) = list(map(int, input().split()))
    odp = [[0] * n for i in range(n)]
    cur = [0, 0]
    zap = 0
    while True:
        if zap >= k:
            break
        odp[cur[0]][cur[1]] = 1
        zap += 1
        cur[0] = (cur[0] + 1) % n
        cur[1] = (cur[1] + 1) % n
        if cur[0] == 0:
            cur[1] = zap // n
    if k % n == 0:
        print(0)
    else:
        print(2)
    for i in range(n):
        print(''.join(list(map(str, odp[i]))))
