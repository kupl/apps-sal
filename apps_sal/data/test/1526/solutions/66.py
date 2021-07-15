A, B, C = map(int, input().split())
maximam = max(A, B, C)
count = (maximam-A)//2 + ( maximam-B)//2 + (maximam-C)//2
A +=((maximam-A)//2*2)
B +=((maximam-B)//2*2)
C +=((maximam-C)//2*2)
if A==B and B == C:
  print(count)
elif (A==B and A==maximam) or (C==B and C==maximam) or (A==C and C==maximam):
  print(count+2)
else:
  print(count+1)
