n, p = list(map(int, input().split()))
s = input()

c = [0 for i in range(p)]
c[0] = 1
x = 0
ans = 0
for i,j in enumerate(s[::-1]):
  if p == 2 or p == 5:
    if int(j)%p == 0:
      ans += n-i
  x = (x + int(j)*pow(10,i,p))%p
  c[x] += 1
if ans:
  print (ans)
  return
for i in range(p):
  ans += (c[i]*(c[i]-1))//2
print (ans)


