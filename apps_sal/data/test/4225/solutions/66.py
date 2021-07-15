a, b, c, k = map(int, input().split())

if k < a:
  print(k)
elif a <= k and k <= a+b:
  print(a)
elif a+b < k:
  c1 = k - (a+b)
  print(a-c1)
