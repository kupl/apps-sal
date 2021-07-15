N, M = list(map(int ,input().split()))

# N + x : M - 2x = 1 : 2
# M - 2x = 2N + 2x
# x = (M - 2N) / 4

if N * 2 >= M:
  print((int(M / 2)))
else:
  x = (M - 2 * N) / 4
  N += int(x)
  M -= 2 * int(x)
  print(N)
  
  

