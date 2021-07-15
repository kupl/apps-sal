n = int(input())

a = [int(input()) for _ in range(n)]
a.insert(0,0)

pos = 1
for i in range(1,n+1):
  pos = a[pos]
  if pos==2:
    print(i)
    break
if pos!=2:
  print((-1))

