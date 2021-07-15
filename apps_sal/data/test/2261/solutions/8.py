def rev(i):
    t=""
    for x in i:
        if x=="+":
            t+="*"
        else:
            t+="+"
    return t
def f(n):
    if n==1:
        return ["++","+*"]
    x=f(n-1)
    p=list(i+i for i in x)
    p=p+list(i+rev(i) for i in x)
    return p
N=int(input())
if N==0:
    print("+")
else:
    t=f(N)
    for i in t:
        print(i)
