n = int(input())
a = list(map(int,input().split()))
b = []

for x in a :
  b.append(1/x)
  
c = sum(b)
ans = 1/c
print(ans)

