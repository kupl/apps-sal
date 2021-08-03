def main():
    N = int(input())
    S = list(input())
    R = []
    G = []
    B = []
    cnt = 0
    for i in range(len(S)):
        if S[i] == "R":
            R.append(i)
        elif S[i] == "G":
            G.append(i)
        elif S[i] == "B":
            B.append(i)
    l = len(B)
    for i in range(len(R)):
        r = R[i]
        for j in range(len(G)):
            g = G[j]
            cnt += l
            if g > r:
                M = g
                m = r
            elif r > g:
                M = r
                m = g
            d = M - m
            if (M + d) < N and S[M + d] == "B":
                cnt -= 1
            if (m - d) >= 0 and S[m - d] == "B":
                cnt -= 1
            if (M + m) % 2 == 0 and S[int((M + m) / 2)] == "B":
                cnt -= 1
    print(cnt)


main()
