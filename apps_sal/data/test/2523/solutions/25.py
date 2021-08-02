def find_cont(S):
    N = len(S)
    res = N
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            res = min([res, max(i + 1, N - 1 - i)])
    return res


S = input()
print((find_cont(S)))
