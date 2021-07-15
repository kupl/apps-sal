def solve():
    H, W = list(map(int, input().split()))
    S = [input() for i in range(H)]

    for i in range(H):
        S[i] = list(S[i])

    for i in range(H):
        for k in range(W):

            if S[i][k]!="#":

                c = 0; #counter

                if i>0 and k>0 and S[i-1][k-1]=="#": # upper left
                    c += 1

                if i>0  and S[i-1][k]=="#": # right above
                    c += 1

                if i>0 and k<W-1 and S[i-1][k+1]=="#": # upper right
                    c+= 1

                if k>0 and S[i][k-1]=="#": # left
                    c += 1
           
                if k<W-1 and S[i][k+1]=="#": # right
                    c += 1

                if i<H-1 and k>0 and S[i+1][k-1]=="#": # lower left
                    c += 1

                if i<H-1 and S[i+1][k]=="#": # right under
                    c += 1

                if i<H-1 and k<W-1 and S[i+1][k+1]=="#": # lower right
                    c += 1

                S[i][k] = str(c)

    for i in range(H):
        print(("".join(S[i])))


def __starting_point():
    solve()


__starting_point()
