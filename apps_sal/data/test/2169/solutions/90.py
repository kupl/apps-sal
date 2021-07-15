H, W, D = map(int, input().split())

x_axis = [0]*(H*W)
y_axis = [0]*(H*W)

for i in range(H):
  A = list(map(lambda x: int(x)-1, input().split()))
  for j in range(W):
    x_axis[A[j]] = j
    y_axis[A[j]] = i

def dis(a, b):
  return abs(x_axis[a]-x_axis[b]) + abs(y_axis[a]-y_axis[b])

magic = [[0] for _ in range(D)]

for i in range(D):
  temp = i
  while temp < H*W-D:
    magic[i].append(magic[i][-1] + dis(temp, temp+D))
    temp += D

Q = int(input())
for _ in range(Q):
  L, R = map(lambda x: int(x)-1, input().split())
  L, d = divmod(L, D)
  R //= D
  print(magic[d][R] - magic[d][L])
