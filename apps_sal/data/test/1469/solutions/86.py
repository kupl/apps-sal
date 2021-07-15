L = int(input())

N = len(str(bin(L)))-2

bitL = [0] *20
splitL  = [0] * 20
sumL = [0] * 20

for i in range(19,-1,-1):
  if L % 2 == 1:
    bitL[i] = 1
  L = L // 2

for i in range(19,-1,-1):
  splitL[i] = int(bitL[i]) * 2**(19-i)

for i in range(20):

  if i == 0:
    sumL[i] = splitL[i]
  else:
    sumL[i] =splitL[i]+sumL[i-1]

#print(splitL)
#print(sumL)
#print(bitL)

edge = []
 
for i in range(N-1):
  edge.append([i+1,i+2,0])
  edge.append([i+1,i+2,2**i])


for i in range(21-N,20):
  if bitL[i] == 1:
    edge.append([20-i,N,sumL[i-1]])


print(N,len(edge))

for i in range(len(edge)):
  print(edge[i][0],edge[i][1],edge[i][2])
