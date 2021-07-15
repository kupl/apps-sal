n,k = map(int,input().split())
p = list(map(int,input().split()))

d_tmp = sum(p[0:k])
d_max = sum(p[0:k])
for i in range(n-k):
  d_tmp = d_tmp + p[k+i] - p[i]
  d_max = max(d_max,d_tmp)

ans = (d_max + k)/2
print(ans)
