n,a,b = map(int,input().split())
ans = 0
for i in range(1,n+1):
    x = list(str(i))
    x = list(map(int,x))
    x = sum(x)
    if a <= x <= b:
        ans += i
print(ans)
