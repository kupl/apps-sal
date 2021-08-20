(N, M) = map(int, input().split())
H = list(map(int, input().split()))
neighbor_max = [0] * N
for _ in range(M):
    (A, B) = map(int, input().split())
    neighbor_max[A - 1] = max(neighbor_max[A - 1], H[B - 1])
    neighbor_max[B - 1] = max(neighbor_max[B - 1], H[A - 1])
ans = 0
for i in range(N):
    if H[i] > neighbor_max[i]:
        ans += 1
print(ans)
