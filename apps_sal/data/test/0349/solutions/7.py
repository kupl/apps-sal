def main():
    (n, m) = map(int, input().split())
    fir = [[] for i in range(n)]
    sec = [[] for i in range(n)]
    for i in range(n):
        fir[i] = list(map(int, input().split()))
    for i in range(n):
        sec[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            (fir[i][j], sec[i][j]) = (min(fir[i][j], sec[i][j]), max(fir[i][j], sec[i][j]))
    for i in range(n):
        for j in range(m):
            if i > 0 and fir[i][j] <= fir[i - 1][j]:
                print('Impossible')
                return 0
            if j > 0 and fir[i][j] <= fir[i][j - 1]:
                print('Impossible')
                return 0
            if i > 0 and sec[i][j] <= sec[i - 1][j]:
                print('Impossible')
                return 0
            if j > 0 and sec[i][j] <= sec[i][j - 1]:
                print('Impossible')
                return 0
    print('Possible')
    return 0


main()
