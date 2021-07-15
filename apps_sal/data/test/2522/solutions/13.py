N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

R = list(reversed(B))
flag = True
for i in range(N):
  if A[i] == R[i]:
    flag = False
    break
if flag:
  print('Yes')
  print(*R)
  return

l1 = B[N//2:]  + B[:N//2]
l2 = B[N//2+1:]  + B[:N//2+1]
flag1 = True
for i in range(N):
  if A[i] == l1[i]:
    flag1 = False
    break
flag2 = True
for i in range(N):
  if A[i] == l2[i]:
    flag2 = False
    break
if (flag1==False) and (flag2==False):
  print('No')
elif flag1 == True:
  print('Yes')
  print(*l1)
else:
  print('Yes')
  print(*l2)
