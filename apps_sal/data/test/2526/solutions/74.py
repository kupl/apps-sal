(X, Y, A, B, C) = list(map(int, input().split()))
P = sorted(map(int, input().split()), reverse=True)[:X]
Q = sorted(map(int, input().split()), reverse=True)[:Y]
R = sorted(map(int, input().split()), reverse=True)
PQ = sorted(P + Q)
ans = sum(PQ)
for (r, pq) in zip(R, PQ):
    if r > pq:
        ans += r - pq
print(ans)
