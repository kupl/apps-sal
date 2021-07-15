N = int(input())
lsd = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += lsd[i]*lsd[j]
print(ans)

