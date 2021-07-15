def f(x):
    x+=1
    while(x%10==0 and x>0):
        x//=10
    return x
vals=set()
n=int(input())
vals.add(n)
while f(n) not in vals:
    vals.add(f(n))
    n=f(n)
print(len(vals))
