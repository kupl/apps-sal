A, B = map(int, input().split())
S = input()
flag = False
for i in range(A):
  if S[i] == "-":
    flag=True
if S[A] != "-":
  flag=True
for i in range(A+1, A+B+1):
  if S[i] == "-":
    flag=True
if flag:
  print("No")
else:
  print("Yes")
