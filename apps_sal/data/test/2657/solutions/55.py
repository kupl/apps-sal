N = int(input())
lsa = list(map(int,input().split()))
n = max(lsa)
r = 0
for i in range(N):
    r1 = lsa[i]
    if min(r1,n-r1) >= min(r,n-r):
        r = r1
print(n,r)
