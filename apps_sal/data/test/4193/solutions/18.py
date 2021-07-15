A_11,A_12,A_13=list(map(int,input().split()))
A_21,A_22,A_23=list(map(int,input().split()))
A_31,A_32,A_33=list(map(int,input().split()))
N=int(input())
Li=[A_11,A_12,A_13,A_21,A_22,A_23,A_31,A_32,A_33]
for i in range(N):
  b=int(input())
  if b in Li:
    Num=Li.index(b)
    Li[Num]=0

if Li[0]==Li[1]==Li[2]==0 or Li[3]==Li[4]==Li[5]==0 or Li[6]==Li[7]==Li[8]:
  print("Yes")
elif Li[0]==Li[3]==Li[6]==0 or Li[1]==Li[4]==Li[7]==0 or Li[2]==Li[5]==Li[8]:
  print("Yes")
elif Li[0]==Li[4]==Li[8]==0 or Li[2]==Li[4]==Li[6]==0:
  print("Yes")
else:
  print("No")

