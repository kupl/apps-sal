n = int(input())
h = list(map(int,input().split()))
count = 0
ans = 0
for i in range(1,n):
    if h[i-1] >= h[i]:
        count += 1
    else:
        ans = max(ans,count)
        count = 0
ans = max(ans,count)
print(ans)
