N = int(input())
S = ""
while N!=0:
  if N&1:
    S = "1"+S
    N = (N-1)//(-2)
  else:
    S = "0"+S
    N = N//(-2)
print(0 if S=="" else S)
