N = int(input())
S = list(input().rstrip())
for i in range(N):
    if S[i] == 'o': S[i] = True
    else: S[i] = False
S.append(S[0])
A = [True] * (N + 2)
for a in [[True, True], [True, False], [False, True], [False, False]]:
    A[0], A[1] = a[0], a[1]
    for j in range(1, N + 1):
        if A[j] ^ S[j]:
            A[j + 1] = not A[j - 1]
        else:
            A[j + 1] = A[j - 1]
    if A[0] == A[-2] and A[1] == A[-1]:
        for k in range(N):
            if A[k]: A[k] = 'S'
            else: A[k] = 'W'
        print("".join(A[:N]))
        return
print(-1)
