import bisect
N = int(input())
A = [int(input()) for i in range(N)]


def lis(S):
    from bisect import bisect_right
    L = [S[0]]
    for s in S[1:]:
        if s >= L[-1]:
            L.append(s)
        else:
            L[bisect_right(L, s)] = s
    return len(L)


print(lis(A[::-1]))
