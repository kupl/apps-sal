N = int(input())
L = list(map(int, input().split()))
sum = 0

for x in range(N):
  for y in range(x+1, N):
    sum += L[x]*L[y]
print(sum)
