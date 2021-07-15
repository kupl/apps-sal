N = int(input())
A = list(map(int,input().split()))

tmp = 0
disc = 0
for i, a in enumerate(A):
  if abs(tmp) < abs(a):
    tmp = a
    disc = i

print(2*N-2)
for i in range(N):
  if i == disc: continue
  print(disc+1, i+1)
if tmp >= 0:
  for i in range(N-1):
    print(i+1, i+1+1)
else:
  for i in range(N-1,0,-1):
    print(i+1, i+1-1)
