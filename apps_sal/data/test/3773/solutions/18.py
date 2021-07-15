import sys
input = sys.stdin.readline

N = int(input())
AK = [list(map(int, input().split())) for _ in range(N)]
# N = 40
# AK = [(i+1, 4) for i in range(N)]

def grundy(A, K):
    if K == 1:
        return A
    X = (A+K-1)//K
    num = X*K - A
    while X*K-num > K*K:
        #print(X, num)
        if num%K == 0:
            return X - num//K
        if num//K == X//K:
            num = num%K
        else:
            num = X%K+1 + (K-1)*(num//K) + (num%K-1)
        X = X - X//K
    
    S = X*K - num
    while S >= K:
        if S%K == 0:
            return S//K
        delta = S//K + 1
        S -= max(((S%K)//delta)*delta, delta)
    return 0
    
g = 0
for A, K in AK:
    # print(A, A//K, grundy(A, K))
    # print()
    g ^= grundy(A, K)

print("Takahashi" if g else "Aoki")
