n = int(input())
t = int(n**(1/2))
a = 0
for i in range(1,t+1):
  if i**2 == n:
    a += i-1
  else:
    if int((n-1)/i) > t:
      a += int((n-1)/i)*2 - t
    else:
      a += int((n-1)/i)
print(a)
