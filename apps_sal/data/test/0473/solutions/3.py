def ui(a):
    a = str(a)
    return '0'*(2-len(a))+a
a,b = map(int,input().split(':'))
c,d = map(int,input().split(':'))
t1 = 60*a+b
t2 = 60*c+d
if t1>=t2:
    dt = t1-t2
else:
    dt = 1440-t2+t1
print(ui(dt//60),':',ui(dt%60),sep='')
