n = int(input())
pt, px, py = 0, 0, 0

for _ in range(n):
  t, x, y = map(int, input().split())
  d = abs(x-px) + abs(y-py)
  if d  > t-pt or (d + t-pt)%2 != 0:
    print("No")
    return
  pt, px, py = t, x, y
print("Yes")
