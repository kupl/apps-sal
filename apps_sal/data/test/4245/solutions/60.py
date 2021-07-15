a,b =map(int,input().split())
x = 1
ans = 0
while x < b:
    x +=a-1
    ans +=1
print(ans)
