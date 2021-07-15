n = int(input())
ts = list(map(int, input().split()))
m = int(input())
for i in range(m):
  p, x = map(int, input().split())
  print(sum(ts) - ts[p-1] + x)
