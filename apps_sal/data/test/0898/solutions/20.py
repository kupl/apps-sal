(N, M) = map(int, input().split())
P = []
A = round(M ** 0.5) + 2
for i in range(1, A):
    if M % i == 0:
        P.append(i)
        P.append(M // i)
P.sort()
B = M // N
ans = now = 1
for p in P:
    now = p
    if now <= B:
        ans = now
print(ans)
