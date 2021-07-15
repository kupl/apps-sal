N = int(input())
An = list(map(int,input().split()))
Bn = list(map(int,input().split()))
sum = 0
for i in range(N):
  if Bn[i] <= An[i]:
    sum += Bn[i]
  elif Bn[i] <= An[i] + An[i + 1]:
    sum += Bn[i]
    An[i + 1] += An[i] - Bn[i]
  else:
    sum += An[i + 1] + An[i]
    An[i + 1] = 0
print(sum)
