n, k, m = map(int, input().split())
aa = list(map(int, input().split()))

sum_aa = sum(aa)
x =n*m -sum_aa
if 0 <= x <= k:
  print(x)
elif x > k:
  print(-1)
elif x < 0:
  print(0)
