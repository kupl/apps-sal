n, a, b = map(int,input().split())
cnt = 0
ans = 0
for x in input():
    if x == '.':
        cnt = cnt+1
    else:
        tmp = cnt//2
        if a > b:
            ans = ans+min(a,cnt-tmp)+min(b,tmp)
            a = max(0,a-cnt+tmp)
            b = max(0,b-tmp)
        else:
            ans = ans+min(a,tmp)+min(b,cnt-tmp)
            a = max(0,a-tmp)
            b = max(0,b-cnt+tmp)
        cnt = 0
tmp = cnt//2
if a > b:
    ans = ans+min(a,cnt-tmp)+min(b,tmp)
    a = max(0,a-cnt+tmp)
    b = max(0,b-tmp)
else:
    ans = ans+min(a,tmp)+min(b,cnt-tmp)
    a = max(0,a-tmp)
    b = max(0,b-cnt+tmp)
print(ans)
