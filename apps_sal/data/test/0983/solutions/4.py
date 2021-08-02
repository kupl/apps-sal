n, p, q, r = map(int, input().split())
A = list(map(int, input().split()))

P = [p * a for a in A]
Q = [q * a for a in A]
R = [r * a for a in A]

ans = - (10 ** 20)

for i in range(1, n):
    P[i] = max(P[i], P[i - 1])

PQ = [0 for i in range(n)]

for i in range(n):
    PQ[i] = P[i] + Q[i]

    if i:
        PQ[i] = max(PQ[i], PQ[i - 1])

for i in range(n):
    ans = max(ans, PQ[i] + R[i])

print(ans)
