N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A)
for i in A:
  if i == B[-1]:
    print(B[-2])
  else:
    print(B[-1])
