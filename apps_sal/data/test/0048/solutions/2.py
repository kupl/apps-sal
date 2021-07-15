def works(X,N,M,K):
    #in each row, how many numbers are < X
    res = 0
    n = 1
    div = X/M
    while n < div:
        res += M
        n += 1
    while n < N+1:
        res += (X-1)//n
        n += 1
    return res

def solve():
    N, M, K = [int(s) for s in input().split()]
    left = 1
    right = K+1
    #we want the smallest smallest such that there are AT LEAST K-1 smaller numbers
    while right - left > 1:
        middle = (left+right)//2
        if works(middle,N,M,K) < K:
            left = middle
        else:
            right = middle
    #if there are exactly K-1 elements less than right, then this is our answer
    return left

#for _ in range(getInt()):    
print(solve())
