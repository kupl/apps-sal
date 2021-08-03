import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(str, input().rstrip().split())) for _ in range(Q)]

for S, T in Query:
    L = len(S)
    update = False
    A = list(S)
    for i in range(L - 1):
        tmp = S[i]
        for j in range(i + 1, L):
            if update and tmp == S[j]:
                ind = j
            if tmp > S[j]:
                tmp = S[j]
                update = True
                ind = j
        if update:
            A[ind] = S[i]
            A[i] = S[ind]
            break
    A_str = "".join(A)
    if A_str < T:
        print(A_str)
    else:
        print("---")
