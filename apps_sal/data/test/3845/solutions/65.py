from pprint import pprint


def create(A, B):
    is_swapped = False
    if(A > B):
        larger = A
        A = B
        B = larger
        is_swapped = True
    H, W = 99, 99
    dp = [['.' for i in range(W)] for j in range(H)]
    Ndot = 1
    Nsharp = 0
    for i in range(1, H - 1, 2):
        for j in range(1, W - 1, 2):
            dp[i][j] = '
            Nsharp += 1

    Nfill = 0
    for i in range(1, H - 2, 4):
        for j in range(1, W - 2, 4):
            if(Nfill == A):
                break
            dp[i + 1][j] = '
            dp[i][j + 1] = '
            dp[i + 2][j + 1] = '
            dp[i + 1][j + 2] = '
            Ndot += 1
            Nsharp -= 3
            Nfill += 1

    for i in range(H):
        for j in range(W):
            if(Nsharp == B):
                break
            else:
                if(i == 0 or i == H - 1 or j == 0 or j == W - 1):
                    continue
                else:
                    if(dp[i][j] == '
                        dp[i][j]='.'
                        Nsharp -= 1

    if(Ndot > A):
        dp[2][1]='.'
        Ndot -= 1


    if(is_swapped):
        for i in range(H):
            for j in range(W):
                if(dp[i][j] == '.'):
                    dp[i][j]= '
                else:
                    dp[i][j]='.'

    Ans=''
    for row in dp:
        tmp=''.join(row)
        tmp += '\n'
        Ans += tmp
    print(*[H, W])
    print(Ans)


a, b=map(int, input().split())
create(a, b)
