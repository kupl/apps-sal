A11,A12,A13 = list(map(int,input().split()))
A21,A22,A23 = list(map(int,input().split()))
A31,A32,A33 = list(map(int,input().split()))

Alist = []
Alist.append(A11)
Alist.append(A12)
Alist.append(A13)
Alist.append(A21)
Alist.append(A22)
Alist.append(A23)
Alist.append(A31)
Alist.append(A32)
Alist.append(A33)
bingolist =[0]*9

N = int(input())
#print (N)
for i in range(N):
  b = int(input())
  #print (b)
  for j in range(len(bingolist)):
    if b ==Alist[j]:
      bingolist[j] = 1

if sum(bingolist[0:3])==3 or sum(bingolist[3:6])==3 or sum(bingolist[6:9])==3 or (bingolist[0]+bingolist[3]+bingolist[6])==3 or (bingolist[1]+bingolist[4]+bingolist[7])==3 or (bingolist[2]+bingolist[5]+bingolist[8])==3 or (bingolist[0]+bingolist[4]+bingolist[8])==3 or (bingolist[2]+bingolist[4]+bingolist[6])==3:
  print ("Yes")
else :
  print ("No")
#print (bingolist[0:3])
#print (bingolist[3:6])
#print (bingolist[6:9])
#print (bingolist)

