n = int(input())
sum = 0

for i in range(2, n + 1):  
  j = 2
  while(j * i <= n):
    sum += i
    j += 1
print(4 * sum)
