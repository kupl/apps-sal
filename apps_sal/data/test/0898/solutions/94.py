N,M = map(int,input().split())

m = 1
ds = set()
while m*m <= M:
    if M%m==0:
        ds.add(m)
        ds.add(M//m)
    m += 1

ans = 1
for d in ds:
    if d*N > M: continue
    ans = max(ans,d)
print(ans)
