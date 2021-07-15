N, M = list(map(int, input().split()))
if N*2 >= M:
  print((M // 2))
  return
ans = N + (M - N*2) // 4
print(ans)

