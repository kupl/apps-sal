N, K = map(int, input().split())

L = [1]
P = [1]

for i in range(N):
    L.append(L[i] * 2 + 3)
    P.append(P[i] * 2 + 1)

def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + L[N-1]:
        return f(N-1, X-1)
    else:
        return P[N-1] + 1 + f(N-1, X-2-L[N-1])

print(f(N, K))
