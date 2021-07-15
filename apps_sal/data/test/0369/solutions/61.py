n, m = map(int, input().split())
s = input()

l = []
cur = n

while cur > 0:
  position = cur
  cur = max(0, cur - m)
  while s[cur] == "1":
    cur += 1
  if cur == position:
    print(-1)
    return
  l.append(str(position - cur))
l.reverse()
print(" ".join(l))
