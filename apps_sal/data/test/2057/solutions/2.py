n = int(input())
l = list(map(int, input().split()))
a = [0 for i in range(200001)]
for x in l:
  a[x] = 1

for i in range(1, 200001):
  n -= a[i]
  
print(n)
