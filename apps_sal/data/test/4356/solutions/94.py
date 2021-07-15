N, M = map(int, input().split())
A = []
B = ""
for _ in range(N):
  A.append(input())
for _ in range(M):
  B += input()
for row in range(N-M+1):
  for col in range(N-M+1):
    tmp = ""
    for p in range(M):
      tmp += A[row+p][col:col+M]
    if tmp == B:
      print("Yes")
      return
print("No")
