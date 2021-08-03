t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if cnt == k:
                break
            board[(j + i) % n][j] = 1
            cnt += 1
        if cnt == k:
            break
    if k % n == 0:
        print(0)
    else:
        maxs = (k + n - 1) // n
        mins = k // n
        print(2 * ((maxs - mins)**2))
    for i in range(n):
        print(''.join(map(str, board[i])))
