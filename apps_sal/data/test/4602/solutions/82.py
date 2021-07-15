N = int(input())
K = int(input())
x = list(map(int,input().split()))
total = 0
for i in range (N):
  if x[i]<K/2:
    total += 2*x[i]
  elif x[i]>= K/2:
    total += 2*(K-x[i])
print(total)
