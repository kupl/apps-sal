n = int(input())
c = n-1
for i in range(1,int(n**0.5)+1):
  if (n/i).is_integer():
    j = n//i
    c = min(c, i+j-2)
print(c)
