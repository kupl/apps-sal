s = int(input())
l = []
def myfunc(x):
  if x%2 == 0:
    x = x//2
  else:
    x = 3*x + 1
  return x
for i in range(10**6):
  l.append(s)
  s = myfunc(s)
  if s in l:
    print(i+2)
    break
