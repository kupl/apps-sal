from math import sqrt
r, h = [int(x) for x in input().split()]
r <<= 1
h <<= 1

ans = h // r * 2
h %= r
if h >= (r // 2):
  ans += 2
  if 3 * r * r <= 4 * h * h:
    ans += 1
else:
  ans += 1
print(ans)

