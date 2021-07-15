N, M = map(int, input().split())
AB = []

for _ in range(M):
  a, b = map(int, input().split())
  AB.append((a, b))

Rsort = sorted(AB, key=lambda x: x[1])
cnt = 0
R = 0

for a, b in Rsort:
  if a <= R:
    continue
  else:
    cnt += 1
    R = b-1

print(cnt)
