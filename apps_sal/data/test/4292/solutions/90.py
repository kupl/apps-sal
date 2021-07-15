N,K = map(int,input().split())
p = sorted([int(i) for i in input().split()])
ans = 0
for i in range(K):
    ans += p[i]
print(ans)
