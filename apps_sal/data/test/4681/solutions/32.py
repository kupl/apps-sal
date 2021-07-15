n = int(input())
luca = [0 for i in range(n+1)]
luca[0] = 2
luca[1] = 1
for j in range(2,n+1):
  luca[j] = luca[j-1] + luca[j-2]
print(luca[n])
