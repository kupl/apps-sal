def main():

    n,m = list(map(int, input().split()))
    S = [list(str(input())) for _ in range(n)]

    L = [[0]*m for _ in range(n)]
    R = [[0]*m for _ in range(n)]
    U = [[0]*m for _ in range(n)]
    D = [[0]*m for _ in range(n)]

    for i in range(n):
        cnt = 0
        for j in range(m):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                L[i][j] = cnt
        cnt = 0
        for j in reversed(list(range(m))):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                R[i][j] = cnt

    for j in range(m):
        cnt = 0
        for i in range(n):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                U[i][j] = cnt
        cnt = 0
        for i in reversed(list(range(n))):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                D[i][j] = cnt

    #print(L)
    #print(R)
    #print(U)
    #print(D)
    #T = [['.']*m for _ in range(n)]
    imosH = [[0]*(m+1) for _ in range(n)]
    imosV = [[0]*m for _ in range(n+1)]
    ans = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if S[i][j] == '.':
                continue
            l = L[i][j]-1
            r = R[i][j]-1
            u = U[i][j]-1
            d = D[i][j]-1
            s = min([l, r, u, d])
            if s == 0:
                continue
            ans.append((i+1, j+1, s))
            imosV[i-s][j] += 1
            imosV[i+s+1][j] -= 1
            imosH[i][j-s] += 1
            imosH[i][j+s+1] -= 1

    #print(imosH)
    #print(imosV)

    from itertools import accumulate
    for i in range(n):
        imosH[i] = list(accumulate(imosH[i]))
    for j in range(m):
        for i in range(1, n+1):
            imosV[i][j] += imosV[i-1][j]

    #print(imosH)
    #print(imosV)

    #print(T)
    for i in range(n):
        for  j in range(m):
            if S[i][j] == '*':
                if imosH[i][j] <= 0 and imosV[i][j] <= 0:
                    print(-1)
                    return
    else:
        print(len(ans))
        for i in range(len(ans)):
            print(*ans[i])

def __starting_point():
    main()

__starting_point()
