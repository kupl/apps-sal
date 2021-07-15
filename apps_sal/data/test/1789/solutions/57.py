a,b,x,y = map(int,input().split())

ans = 0

if a > b:
    if 2*x > y:
        ans = (a-b-1)*y+x
    else:
        ans = (a-b)*x*2-x
else:
    if 2*x > y:
        ans = (b-a)*y+x
    else:
        ans = (b-a)*x*2+x
print(ans)
