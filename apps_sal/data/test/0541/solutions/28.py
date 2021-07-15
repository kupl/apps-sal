n, m = map(int, input().split())

bridge = [None]*m
for i in range(m):
  a, b = map(int, input().split())
  bridge[i] = [b, a]

ans = 0
bridge.sort()

sub = -1
ans = 0
for v in bridge:
  b, a = v[0], v[1]
  if a >= sub:
    sub = b
    ans += 1

print(ans)
