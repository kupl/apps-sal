n,m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
count = 0
for i in range(1, n-1):
  suma = a[i-1]+a[i]
  if suma > m:
    count += suma - m
    if a[i] > suma-m:
      a[i]-= suma - m
    else:
      a[i-1] -= suma-m-a[i]
      a[i] = 0
  #print(i, count, a)
else:
  if a[-1]+a[-2] > m:
    count += a[-2] + a[-1]-m
    a[-1] -= a[-2] + a[-1]-m
#print(a, count)
if n <= 2:
  if count + sum(a)-m >= 0:
    print(count + sum(a)-m)
  else:
    print(0)
else:
  print(count)
