(N, K) = list(map(int, input().split()))
S = list(input())
T = ['R', 'P', 'S']
for i in range(N):
    S[i] = T.index(S[i])
for _ in range(K):
    S += S
    tmp = []
    for i in range(0, len(S), 2):
        (a, b) = (S[i], S[i + 1])
        (a, b) = (max(a, b), min(a, b))
        if a == 2 and b == 0:
            x = b
        else:
            x = a
        tmp.append(x)
    S = tmp
print(T[S[0]])
