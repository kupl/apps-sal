import sys

N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

cnt = 0
for i in range(N-1):
  if A[i] - A[i+1] == 0:
    cnt +=1
if cnt < 2:
  print("0")
  return

leng1 = 0
leng2 = 0
diff = 10**9

i = 0
while diff != 0:
  diff = A[i] - A[i+1]
  i += 1  
leng1= A[i]

A.remove(leng1)
A.remove(leng1)

i = 0
diff = 10**9
while diff != 0:
  diff = A[i] - A[i+1]
  i += 1  
leng2= A[i]

print(leng1*leng2)
