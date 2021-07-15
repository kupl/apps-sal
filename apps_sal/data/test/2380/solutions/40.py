n, m  = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cb = []
for i in range(m):
  b, c = map(int, input().split())
  cb.append([c,b])
cb.sort(reverse=True)

j = 0
for i in range(m):
  k = 0
  while k<cb[i][1] and k+j<n and a[k+j]<cb[i][0]:
    a[k+j] = cb[i][0]
    k += 1
  j += k
  if j == n:
    break
    
print(sum(a))
