from itertools import accumulate
n,k = map(int,input().split())
a = list(map(int,input().split()))
suma = sum(a)
devisor = []
for i in range(1,int(suma**0.5)+1):
  if suma%i == 0:
    devisor.extend((i,suma//i))
devisor.sort(reverse=True)
for x in devisor:
  b = [a[i]%x for i in range(n)]
  b.sort()
  sumb = list(accumulate(b))
  for y in range(n-1):
    bf = sumb[y]
    bl = sumb[n-1]-sumb[y]
    if bf%x == (x-(bl%x))%x:
      if k>=max(bf,(n-1-y)*x-bl):
        print(x)
        return
      else:
        continue
