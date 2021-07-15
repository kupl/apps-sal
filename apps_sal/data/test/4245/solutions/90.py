n = 0
a, b = map(int, input().split())
while n*(a-1)+1 < b:
  n += 1
 
print(n)
