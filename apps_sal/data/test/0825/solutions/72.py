N = int(input())
D = {}

for k in range(2,10**6):
  while N%k<1:
    N//=k
    D[k]=D.get(k,0)+1

a = 0
for i in D.values():
  t = 0
  c = 0
  while t+c<i:
    c+=1
    t+=c
  a+=c
print(a+(N>1))
