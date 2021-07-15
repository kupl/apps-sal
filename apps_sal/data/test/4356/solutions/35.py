import sys
N,M=map(int,input().split())
A=[]
for i in range(N):
  a=input()
  A.append(a)
B=[]
for j in range(M):
  b=input()
  B.append(b)
for k in range(N-M+1):
  for l in range(N-M+1):
    z=0
    for m in range(M):
      try:
        if B[m]==A[k+m][l:l+M]:
          z+=1
      except:
        sys.stderr.write(f"{k,l,m}")
        pass
    if z==M:
      print("Yes")
      return
print("No")
