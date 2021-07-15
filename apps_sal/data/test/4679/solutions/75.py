a,b,c = [str(input()) for i in range(3)]
current = 'a'
while True:
  try:
    cur = current[len(current)-1]
    if cur == 'a':
      current+=a[0]
      a=a[1:]
    elif cur == 'b':
      current+=b[0]
      b=b[1:]
    elif cur == 'c':
      current+=c[0]
      c=c[1:]
  except:
      print(current[len(current)-1].upper())
      break
