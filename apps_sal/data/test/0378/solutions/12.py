n,m = (int(i) for i in input().split())
ans = 10
for i in range(1,10):
    if (n*i-m)%10 == 0 or (n*i)%10 == 0:
        ans = min(ans,i)
print(ans)
