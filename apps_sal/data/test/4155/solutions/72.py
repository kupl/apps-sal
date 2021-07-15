n = int(input())
h = list(map(int, input().split()))

cnt = 0

a = 0
for i in range(n-1):
  if h[i+1] < h[i]:
    cnt += h[i]-a
    a = h[i+1]
cnt += h[-1]-a
print (cnt)

