n, m = map(int, input().split())
a = input().split()
x = a.count("-1")
ans = ""
for _ in range(m):
  l, r = map(int, input().split())
  if (r-l) % 2 == 1 and min(x, n-x) >= (r-l+1)//2:
    ans += "1\n"
  else:
    ans += "0\n"
print(ans)
