n = input()
p = 2019
t = 1
y = 0
c = p*[0]

for x in map(int,n[::-1]):
  y+=t*x
  y%=p
  c[y]+=1
  t*=10
  t%=p

print(sum(i*(i-1)//2 for i in c)+c[0])
