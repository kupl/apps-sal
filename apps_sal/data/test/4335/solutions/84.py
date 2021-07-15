N = int(input())
A = str(input())

if (N % 2 == 0):
  if (A[:N//2] == A[N//2:]):
    print("Yes")
  else:
    print("No")
else:
  print("No")

