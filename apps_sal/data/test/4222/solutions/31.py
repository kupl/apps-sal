n, k = map(int, input().split())
a = set({})
for i in range(k):
  d = int(input())
  for j in input().split():
  	a.add(j)
print(n - len(a))    
