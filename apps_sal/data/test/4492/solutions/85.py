n,x = map(int, input().split())
a = list(map(int, input().split()))

t = 0
ans = 0
for i in a:
  s = max(0, t+i-x) # 一つ前の値の差分を含めて、xとの差分を取得し、比較
  t = i - s
  ans += s
print(ans)
