n=int(input())
A=[int(x) for x in input().split()]

u=10**6+1
C=[0]*u
D=[0]*2+[1]*(u-2)

def gcd(a,b):
   while a%b:
     a,b=b,a%b
   return b

n=4
while n<u:
  D[n]=0
  n+=2
i=3
while i*i<u:
  if D[i]:
    n=i*2
    while n<u:
      D[n]=0
      n+=i
  i+=2

for a in A:
  C[a]+=1
for i in [x for x in range(2,u) if D[x]==1]:
  if sum(C[i::i])>1:
    break
else:
  print('pairwise coprime')
  return

c=A[0]
for a in A:
  c=gcd(c,a)
  if c==1:
    break
else:
  print('not coprime')
  return

print('setwise coprime')

