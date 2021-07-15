N, M = map(int, input().split())
A = [0]*(N+1)
W = A.copy()
for _ in range(M):
    P, S = input().split()
    p = int(P)
    if S == "AC":
        A[p] = 1
    elif A[p] == 0:
        W[p] += 1

print(sum(A), sum(a*w for a, w in zip(A, W)))
