def divisor(n):
  cd = []
  i = 1
  while i*i <= n:
    if n%i==0:
      cd.append(i)
      if i != n//i:
        cd.append(n//i)
    i += 1
  return cd

N, M = map(int, input().split())
cd = divisor(M)
cd.sort(reverse=True)
for c in cd:
  if M//c>=N:
    print(c)
    break
