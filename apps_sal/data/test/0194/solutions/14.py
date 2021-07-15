n,a,b = list(map(int,input().split()))
arr = [int(x) for x in input().split()]
ans = 0
ca = 0
for i in arr:
    if i==1:
        if a!=0:
            a -= 1
        elif b!=0:
            b -= 1
            ca += 1
        elif ca!=0:
            ca -= 1
        else:
            ans += 1
    else:
        if b!=0:
            b -= 1
        else:
            ans += 2
print(ans)

