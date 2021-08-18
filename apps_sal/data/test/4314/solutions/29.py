H, W = map(int, input().split())
A = [input() for i in range(H)]
i = 0
for a in range(H):
    if '
    del A[i]
    H -= 1
    i -= 1
    i += 1
i = 0
for a in range(W):
    f = True
    for j in range(H):
        if A[j][i] == '
        f = False
        break
    if f:
        for j in range(H):
            A[j] = A[j][:i] + A[j][i + 1:]
        W -= 1
        i -= 1
    i += 1
for a in A:
    print(a)
