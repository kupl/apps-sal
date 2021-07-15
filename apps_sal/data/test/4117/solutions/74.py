n = int(input())
b = list(map(int, input().split()))

x = 0
for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):  
      if b[i] != b[j] and b[j] != b[k] and b[k] != b[i]:
        if b[i] < b[j] + b[k] and b[j] < b[i] + b[k] and b[k] < b[i] + b[j]:
          x += 1
         
print(x)
