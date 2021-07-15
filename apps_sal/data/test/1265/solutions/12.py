x=list(input())
y=list(input())
if len(x)!=len(y):
    print('NO')
    raise SystemExit
    
if x.count('1')==0 and y.count('1')==0:
    print('YES')
    raise SystemExit

if x.count('1')>0 and y.count('1')>0:
    print('YES')
    raise SystemExit    
    
print('NO')
