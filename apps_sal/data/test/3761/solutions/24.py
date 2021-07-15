*s, = map(len,input().split("T"))
x,y = map(int,input().split())

def solve(a,x):
    x = abs(x)+sum(a)
    dp = 1
    for i in a:
        dp |= dp<<(2*i)
    return dp>>x&1

if solve(s[2::2],x-s[0]) and solve(s[1::2],y):
    print("Yes")
else:
    print("No")
