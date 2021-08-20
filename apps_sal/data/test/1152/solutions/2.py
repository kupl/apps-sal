def main():
    (n, m) = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    kek = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] ^= kek[i][j]
    f = 1
    for i in range(n):
        s = 0
        for j in range(m):
            s += arr[i][j]
        if s & 1:
            f = 0
            break
    for i in range(m):
        s = 0
        for j in range(n):
            s += arr[j][i]
        if s & 1:
            f = 0
            break
    if f:
        print('Yes')
    else:
        print('No')
    return 0


main()
