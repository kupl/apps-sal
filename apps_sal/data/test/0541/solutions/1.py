N,M = map(int,input().split())
W = sorted([list(map(int,input().split())) for m in range(M)],key=lambda x:x[1])
c = 0
x = 0

for a,b in W:
   if x<a:
      x=b-1
      c+=1

print(c)
