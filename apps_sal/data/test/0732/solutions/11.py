n=int(input())
a=[]
def foo(x,i,j):
    if x>n:
        return
    if x:
        a.append(x)
    if 10*x+i!=x:
        foo(10*x+i,i,j)
    foo(10*x+j,i,j)
for i in range(10):
    for j in range(i+1,10):
        foo(0,i,j)
print(len(set(a)))

