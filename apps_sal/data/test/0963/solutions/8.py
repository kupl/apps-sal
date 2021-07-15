def main():
    CONST = 998244353
    N,K = list(map(int,input().split()))
    lis = [0]*N*3
    MoveLis = []
    SumLis = [0]*N*3
    for i in range(K):
        L,R = list(map(int,input().split()))
        MoveLis.append((L,R))
    lis[1] = 1
    SumLis[1] = 1
    for i_n in range(2,N+1):
        for i_k in range(K):
            lis[i_n] += SumLis[max(i_n-MoveLis[i_k][0],0)] - SumLis[max(i_n-MoveLis[i_k][1]-1,0)]
            lis[i_n] %= CONST
        SumLis[i_n] += SumLis[i_n -1] + lis[i_n]
        SumLis[i_n] %= CONST
    print((lis[N]))
             




def __starting_point():
    main()


__starting_point()
