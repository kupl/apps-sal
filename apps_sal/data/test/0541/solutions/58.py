N,M = map(int,input().split())
arr = []
for _ in range(M):
  a,b = map(int,input().split())
  arr.append((a,b))
arr.sort(key=lambda x: x[1])
ans = 1
_, pb = arr[0]
for a,b in arr[1:]:
  if pb <= a:
    ans += 1
    pb = b
print(ans)
