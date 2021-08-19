(N, M) = list(map(int, input().split()))
(a, b) = (0, N)
for _ in range(M):
    (tmpa, tmpb) = list(map(int, input().split()))
    (a, b) = (max(a, tmpa), min(b, tmpb))
ans = max(0, b - a + 1)
print(ans)
