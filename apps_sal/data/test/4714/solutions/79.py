a,b = map(int,input().split())
ans = 0
for i in range(a,b+1):
    x = str(i)
    y = x[::-1]
    if x == y:
        ans += 1
print(ans)
