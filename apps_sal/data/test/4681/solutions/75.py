n = int(input())

a = [2,1]

for x in range(n-1):
  a.append(a[x] + a[x+1])
  
print(a[-1])
