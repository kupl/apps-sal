from itertools import product

ans = -10**9 - 1

N = int(input())
F = []
for _ in range(N):
  F.append(list(map(int, input().split())))

P = []
for _ in range(N):
  P.append(list(map(int, input().split())))

all_x = True
for ox in product((0, 1), repeat=10):
  if all_x:
    all_x = False
  else:
    temp = 0
    for n in range(N):
      cnt = 0
      for i, j in zip(F[n], ox):
        cnt += i*j
      temp += P[n][cnt]
    ans = max(ans, temp)

print(ans)
