q=int(input())
a=[int(input()) for i in range(0,q)]
def f(w):
    if w in [1,2,3,5,7,11]:
        return -1
    g=0
    if w%2==1:
        w-=9
        g=1
    return w//4+g
for i in a:
    print(f(i))
