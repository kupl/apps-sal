import math
N = int(input())
if N == 0:
  print(0)
  return
p = int(math.log2(abs(N))) + 1
ans = [0] * (p + 10)
now = 0
for i in range(p + 10):
  x = N % (2 ** (i + 1))
  y = (now + ((-1) ** i) * (2 ** i) ) % (2 ** (i + 1))
  if (y == x) or (y + 2 ** (i + 1) == x):
    now += ((-1) ** i) * (2 ** i)
    ans[i] = 1
  if now == N:
    break
  #print(now, ans, x, y)

#print("n", now, ans, x, y)
p = 0
for i in range(1, len(ans) + 1):
  if p == 0:
    if ans[-i] != 0:
      p = 1
      print(ans[-i], end = "")
  else:
    print(ans[-i], end = "")

print("")


