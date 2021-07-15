A,B,C,D = map(int,input().split())

if A==B+C+D or B==A+C+D or C==A+B+D or D==A+B+C:
  print("Yes")
elif A+B==C+D or A+C==B+D or A+D==B+C:
  print("Yes")
else:
  print("No")
