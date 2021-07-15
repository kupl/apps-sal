n = int(input())
p = list(map(int, input().split()))
k = int(input())
for i in range(k):
  a, b = list(map(int, input().split()))
  c = p[a-1]
  p[a-1] = b
  print((sum(p)))
  p[a-1] = c

