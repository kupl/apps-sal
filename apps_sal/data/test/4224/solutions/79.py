n = int(input())
A = list(map(int,input().split()))
c = 0
for i in A:
  while i%2 == 0:
    i = i//2
    c+=1
print(c)
