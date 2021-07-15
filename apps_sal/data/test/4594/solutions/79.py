N = int(input())
d = []
for i in range(0,N):
  d += [int(input())]

d.sort(reverse=True)

ans = 0

x = max(d)+1
for i in range(0,N):
  
  if d[i] < x:
    ans += 1
    x = d[i]

print(ans)
