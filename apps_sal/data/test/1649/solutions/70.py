A,B,C,D = sorted(map(int,input().split()))

if A+B+C==D or A+D==B+C:
  print("Yes")
else:
  print("No")
