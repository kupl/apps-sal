x = int(input())

idx = x//11
ans = idx*2

if x%11 != 0:
  ans += 2
if 0 < x%11 and x%11 <= 6:
  ans -= 1
print(ans)
