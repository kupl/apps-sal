A,B,X = map(int,input().split())
if(A+B > X):
    print(0)
    return
a = 0
b = 10**9+1
while(a+1 < b):
    m = (a+b)//2
    if(A*m+B*len(str(m)) == X):
        print(m)
        return
    if(A*m+B*len(str(m)) > X):
        b = m
    if(A*m+B*len(str(m)) < X):
        a = m
print(a)
