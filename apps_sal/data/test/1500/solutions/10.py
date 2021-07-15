n, k = map(int, input().split())
v = list(map(int, input().split()))

cnt = 1
moved = 0

for i in range(1, n):
  if v[i]-v[i-1] > k:
    print(-1)
    return
  if v[i]-v[i-1]>k-moved:
    #print("get at", v[i-1])
    cnt += 1
    moved = v[i]-v[i-1]
  else:
    moved += v[i]-v[i-1]
    
print(cnt)
