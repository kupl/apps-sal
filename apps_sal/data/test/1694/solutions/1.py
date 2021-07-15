n,m,s,f = map (int, input().split())
watch = {}
for i in range (m):
  t,l,r = map (int, input().split())
  watch[t] = (l,r)
cur = s
move,symbol = (1,'R') if s < f else (-1,'L')
step = 1
while cur != f:
  if step in watch:
    l,r = watch[step]
    if (l <= cur <= r or
        l <= (cur+move) <= r):
      print ('X',end='')
    else:
      cur += move
      print (symbol,end='')
  else:
    cur += move
    print (symbol,end='')
  step += 1

