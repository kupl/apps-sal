C1 = list(map(int,input().split()))
C2 = list(map(int,input().split()))
C3 = list(map(int,input().split()))

if C1[0]-C1[1]==C2[0]-C2[1]==C3[0]-C3[1] and C1[1]-C1[2]==C2[1]-C2[2]==C3[1]-C3[2] and C1[0]-C2[0]==C1[1]-C2[1]==C1[2]-C2[2] and C2[0]-C3[0]==C2[1]-C3[1]==C2[2]-C3[2]: 
  print("Yes")
else:
  print("No")
