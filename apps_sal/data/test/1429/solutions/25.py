def hoge():
    (N, S) = input().split()
    N = int(N)
    ans = 0
    for i in range(N):
        (at, cg) = (0, 0)
        for j in range(i, N):
            X = S[j]
            if X == 'A':
                at += 1
            elif X == 'T':
                at -= 1
            elif X == 'C':
                cg += 1
            else:
                cg -= 1
            if at == 0 and cg == 0:
                ans += 1
    print(ans)


hoge()
