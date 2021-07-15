N = int(input())
L = list(map(int, input().split()))

L.sort()
length = 0
for i in range(N-1):
  length += L[i]
if length > L[N-1]:
  print('Yes')
else:
  print('No')
