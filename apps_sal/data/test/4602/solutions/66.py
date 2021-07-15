n = int(input())
k = int(input())

s = 0
xs = list(map(int, input().split()))
for x in xs:  
  if x < abs(k-x):
    s += 2 * x
  else:
    s += 2 * abs(k-x)
    
print(s)

