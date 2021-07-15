t=int(input())
def fun(n):

    a=bin(2*n)[2:]
    ans=0
    for i in a:
        if i=="1":
            ans+=1
    print(2*n-ans)
while t:
    t-=1
    n=int(input())
    fun(n)

