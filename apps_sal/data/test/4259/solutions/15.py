K = int(input())
A,B = map(int, input().split())

for num in range(A, B+1, 1):
  if num % K == 0:
    print('OK')
    break
else:
  print('NG')
