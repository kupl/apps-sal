#  --*-coding:utf-8-*--


def f(N, M, S, T):
    W = [1]*(N+1)

    for i, t in enumerate(T):
        W2 = W[:]
        
        k = 0
        for j, s in enumerate(S):
            if t == s:
                k += W[j]

            x = (W2[j+1] + k)%1000000007
            W2[j+1] = x

        W = W2
        
    return W[-1]



def main():
    N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    print((f(N,M,S,T)))



def __starting_point():
    main()


__starting_point()
