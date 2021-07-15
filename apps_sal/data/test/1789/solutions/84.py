a,b,x,y = list(map(int,input().split()))

ans = x
if a==b:
    print(ans)
elif a>b:
    print((ans + (a-1-b)*min(2*x,y)))
else:
    print((ans + (b-a)*min(2*x,y)))

