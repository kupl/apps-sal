a = [6,2,5,5,4,5,6,3,7,6]

def foo(x):
    t = len(str(x))
    res = 0
    for i in range(t):
        res+=a[x%10]
        x//=10
    return res
ans = 0
x,y = map(int,input().split())
for i in range(x,y+1):
    ans+=foo(i)
print(ans)
