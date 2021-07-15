N = int(input())
sum = 0
for i in range(N):
  l, r = map(int, input().split())
  sum += (r-l) + 1
  
print(sum)
