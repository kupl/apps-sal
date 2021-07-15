n = int(input())
prizes = list(map(int, input().split()))

res = 0
for pos in prizes:
  res = max(res, min(pos-1, 10**6-pos))

print(res)

