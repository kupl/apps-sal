A, B, C, K = map(int, input().split())


def ans167(A, B, C, K):
    if A >= K:
        return(K)
    elif A + B >= K:
        return(A)
    else:
        return(A - (K - A - B))


print(ans167(A, B, C, K))
