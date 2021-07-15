N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
adj_max = [0]*N
ans = 0
for _ in range(M):
  tmp1, tmp2 = list(map(int, input().split()))
  adj_max[tmp1-1] = max(adj_max[tmp1-1], H[tmp2-1])
  adj_max[tmp2-1] = max(adj_max[tmp2-1], H[tmp1-1])
for num in range(N):
  if H[num] > adj_max[num]:
    ans += 1
print(ans)


