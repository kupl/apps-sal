s = input()
plus = s.index('+')
ravno = s.index('=')
a = len(s[:plus])
b = len(s[plus+1:ravno])
c = len(s[ravno+1:])
if a+b == c-2:
    a += 1
    c -= 1
    print('|'*a,'+','|'*b,'=','|'*c,sep='')
elif a+b-2 == c:
    c +=1
    if a>1:
        a -= 1
        print('|'*a,'+','|'*b,'=','|'*c,sep='')
    elif b>1:
        b -= 1
        print('|'*a,'+','|'*b,'=','|'*c,sep='')
elif a+b == c:
    print('|'*a,'+','|'*b,'=','|'*c,sep='')    
else:
    print('Impossible')
