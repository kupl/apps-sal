n = int(input())
a = list(map(int,input().split()))
box = set([])
for i in range(n,0,-1):
  cnt = 0
  for j in range(1,n//i+1):
    if i*j in box:
      cnt += 1
  if cnt%2 != a[i-1]:
    box.add(i)
print(len(box))
print(*box)
