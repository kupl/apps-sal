n = int(input())
k = int(input())
data = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans += min(data[i]*2, (k - data[i])*2)
print(ans)
