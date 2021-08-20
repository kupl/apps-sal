for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] % 2 != (i + j) % 2:
                arr[i][j] += 1
    for r in arr:
        print(*r)
