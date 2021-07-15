n,x = map(int, input().split())
l = []
for i in range(n):
  l.append(int(input()))
r = x-sum(l)
print(n+r//min(l))
