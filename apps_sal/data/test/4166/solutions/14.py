def f():
  n, m = map(int, input().split())
  num = [set() for i in range(n)]
  for i in range(m):
    s, c = map(int, input().split())
    num[s-1].add(c)
  s = []
  for i in num:
    if len(i) > 1:
      print(-1)
      return
    if len(i) == 1:
      for x in i:
        s.append(x)
        break
    else:
      s.append(0)
  if s[0] == 0 and n != 1:
    if len(num[0]) > 0:
      print(-1)
      return
    else:
      s[0] = 1
  print(''.join(str(x) for x in s))
f()
