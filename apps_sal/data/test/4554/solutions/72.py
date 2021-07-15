w,a,b = list(map(int,input().split()))
ans = 0
if a+w<b:
    ans = b-(a+w)
elif b<a:
    ans = a-(b+w)
else:
    ans = 0
print(ans)

