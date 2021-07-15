def main():
    n, m = map(int, input().split())

    a = [[] for i in range(n)]
    b = [[] for i in range(n)]
    aDicts = [dict() for i in range(n + m - 1)]
    bDicts = [dict() for i in range(n + m - 1)]    
    
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        b[i] = list(map(int, input().split()))

    for i in range(n):
        for j in range(m):
            if a[i][j] in aDicts[i + j].keys():
                aDicts[i + j][a[i][j]] += 1
            else:
                aDicts[i + j][a[i][j]] = 1
    
            if b[i][j] in bDicts[i + j].keys():
                bDicts[i + j][b[i][j]] += 1
            else:
                bDicts[i + j][b[i][j]] = 1            

    for i in range(n + m - 1):
        if aDicts[i] != bDicts[i]:
            print("NO")
            return 0
    print("YES")
    return 0

main()
