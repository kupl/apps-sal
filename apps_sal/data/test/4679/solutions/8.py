a,b,c = [input() for i in range(3)]
sa = 'a'
for i in range(1796):
  try:
    if sa ==  'a':
      sa = a[0]
      a = a[1:]

    elif sa ==  'b':
      sa = b[0]
      b = b[1:]

    elif sa ==  'c':
      sa = c[0]
      c = c[1:]
  except:
    print(sa.upper())
    break
