a, b, c = map(int, input().split())
x = max(a,b,c)
y = (x-a)+(x-b)+(x-c)
if y%2==1:
  y += 3
  
print(y//2)
