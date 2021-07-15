n,m = list(map(int,input().split()))
x = [list(map(int,input().split())) for l in range(n)]
x = sorted(x)
count = m
p = 0
for i in x:
  if count >= i[1]:
    count -= i[1]
    p += i[0] * i[1]
  elif count ==0:
    break
  else:
    p += i[0] * count
    count = 0

print(p)

