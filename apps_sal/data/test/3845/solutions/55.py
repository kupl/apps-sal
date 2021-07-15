
G=[["#"]*100 for i in range(100)]
for i in range(50,100):
  for j in range(100):
    G[i][j]="."

A,B=map(int,input().split())   
A-=1
B-=1

i,j=0,0

while(A>0):
  G[i][j]="."
  A-=1
  j+=2
  if j>99:
    j=0
    i+=2
i,j=99,0
while(B>0):
  G[i][j]="#"
  B-=1
  j+=2
  if j>99:
    j=0
    i-=2
    
    
print(100,100)
for i in range(100):
  print("".join(G[i]))
