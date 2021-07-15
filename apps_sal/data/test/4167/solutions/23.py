n,k = map(int,input().split())
if k%2 == 1:
    ans = (n//k)**3
else:
    if k <= 2*n:
        a = (n//(k//2))
        b = a//2
        ans = (a-b)**3 + b**3
    else:
        ans = 0
print(ans)
