N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [a1 ^ a2 for (a1, a2) in zip(A, A[1:])] + [A[0] ^ A[-1]]
C = C + C
D = [b1 ^ b2 for (b1, b2) in zip(B, B[1:])] + [B[0] ^ B[-1]]
K = []
k = 0
while k < N:
    next_k = k
    is_first = True
    for i in range(N):
        if is_first and i > 0 and (C[k + i] == D[0]):
            next_k = k + i
            is_first = False
        if C[k + i] != D[i]:
            if next_k == k:
                k = k + i + 1
            elif D[k + i - next_k] == C[k + i]:
                k = next_k
            else:
                k = k + i + 1
            break
    if i == N - 1:
        K.append(k)
        if next_k == k:
            break
        else:
            k = next_k
            if len(K) == 2:
                diff = K[1] - K[0]
                while K[-1] < N:
                    K.append(K[-1] + diff)
                _ = K.pop()
                break
for k in K:
    print(k, A[k] ^ B[0])
