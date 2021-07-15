def su(n):
  return sum(list(map(int,list(str(n)))))
N=int(input())
if N%su(N)==0:
  print("Yes")
else:
  print("No")
