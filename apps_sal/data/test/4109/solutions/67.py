N, M, X = map(int, input().split())

C = []
A = []

for _ in range(N):
    q = list(map(int, input().split()))

    C.append(q[0])
    A.append(q[1:])

#bit全探索

ans = 1300000

for bit in range(1 << N):
    acquire = [0] * M
    cost = 0
    for i in range(N):
        if (bit >> i) % 2 == 1:
            cost += C[i]
            acquire = [a + b for a, b in zip(acquire, A[i])]

    if min(acquire) >= X:
        ans = min(ans, cost)

if ans == 1300000:
    ans = -1

print(ans)
