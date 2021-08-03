N, M = list(map(int, input().split()))
t = [0 for i in range(M + 1)]
for i in range(N):
    A = list(map(int, input().split()))
    for j in range(1, A[0] + 1):
        t[A[j]] += 1
ans = 0
for i in t:
    if i == N:
        ans += 1
print(ans)
