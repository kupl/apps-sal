a,b = map(int,input().split())
ans = 0
for i in range(a,b+1):
    c = str(i)
    if c[0] == c[4] and c[1] == c[3]:
        ans += 1
print(ans)
