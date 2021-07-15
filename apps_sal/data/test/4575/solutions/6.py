n, d, x, *a = map(int, open(0).read().split())
ans = x
for i in a:
  ans += (d - 1) // i + 1
print(ans)
