N, C = map(int, input().split())
rec = [[0]*C for _ in range(10**5)]
for _ in range(N):
  s, t, c = map(int, input().split())
  for i in range(s-1, t):
    rec[i][c-1] = 1

print(max([sum(rec[i]) for i in range(10**5)]))
