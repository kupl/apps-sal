N = int(input())
h = list(map(int,input().split()))
ans = h[0]
for i in range(1,N):
    if h[i] > h[i-1]:
        ans += h[i] - h[i-1]
print(ans)
