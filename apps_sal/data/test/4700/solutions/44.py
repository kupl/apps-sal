N, M = map(int, input().split())
H = list(map(int, input().split()))

# N,M=O(10^5)なので、O(N+M)で解く
# 各ノードについて、隣接する展望台の高さの最大値を更新する
neighbor_max = [0] * N
for _ in range(M):
  A, B = map(int, input().split())
  neighbor_max[A - 1] = max(neighbor_max[A - 1], H[B - 1])
  neighbor_max[B - 1] = max(neighbor_max[B - 1], H[A - 1])

# 各ノードについて、自身の高さと、隣接する展望台の高さの最大値を比較する
# 接続を一つも持たないノードについても、計算は正しい
ans = 0
for i in range(N):
  if H[i] > neighbor_max[i]: ans += 1
    
print(ans)
