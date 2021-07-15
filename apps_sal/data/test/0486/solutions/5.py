def s(a):
    a=list(a)
    while a and a[0]=='0':
        a.pop(0)
    prod=1 
    for i in a:
        
        prod*=int(i)
    return prod 
a=input()
ans=[s(a),a]
for i in range(len(a)-1, -1, -1):
    if a[i]=='0':continue
    b=a[:i] + str(int(a[i])-1) + "9"*len(a[i+1:])
    if s(b) > ans[0]:
        ans=[s(b),b]
print(int(ans[0]))
