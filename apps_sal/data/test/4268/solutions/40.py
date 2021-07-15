from math import sqrt

N, D = [int(i) for i in input().split()]

XS = [list(int(i) for i in input().split()) for _ in range(N)]

cnt = 0
for i in range(N):
  for j in range(i+1, N):
    if sqrt(sum((y - z) ** 2 for y, z in zip(XS[i], XS[j]))).is_integer():
      cnt += 1
      
print(cnt)

