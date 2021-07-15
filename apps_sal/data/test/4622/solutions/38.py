N = int(input())
A = list(map(int, input().split()))

A_set = set(A)

if len(A) == len(A_set):
  print('YES')
else:
  print('NO')
