n,k = map(int,input().split())
counter = 0
while(n >= k):
  n = n//k
  counter = counter + 1
print(counter+1)
