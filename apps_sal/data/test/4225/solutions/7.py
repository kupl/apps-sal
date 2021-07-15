a, b, c, k = map(int, input().split())

if a >= k:
  print(k)
  return
elif a+b >=k:
  print(a)
  return
elif a+b+c >=k:
  print(2*a + b -k)
  return
else:
  print(a-c)
