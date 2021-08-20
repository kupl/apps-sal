(N, M) = map(int, input().split())
H = list(map(int, input().split()))
mx = [0 for i in range(N)]
for _ in range(M):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    mx[a] = max(mx[a], H[b])
    mx[b] = max(mx[b], H[a])
ans = 0
for i in range(N):
    if H[i] > mx[i]:
        ans += 1
print(ans)
