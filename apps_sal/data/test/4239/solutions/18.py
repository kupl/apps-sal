n=int(input())
def f(x):
    ans=0
    while x>0:
        ans+=x%6
        x=x//6
    return ans
def g(x):
    ans=0
    while x>0:
        ans+=x%9
        x=x//9
    return ans
ans=n
for i in range(n+1):
    ans=min(ans,f(i)+g(n-i))
print(ans)

