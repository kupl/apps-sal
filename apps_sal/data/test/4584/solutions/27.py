N = int(input())
A = list(map(int, input().split()))

result = [0] * N

for a in A:
  result[a-1] += 1
  
for i in range(N):
  print((result[i]))

