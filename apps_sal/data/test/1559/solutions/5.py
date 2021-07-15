


"""
NTC here
"""
from sys import setcheckinterval, stdin, setrecursionlimit
setcheckinterval(1000)
setrecursionlimit(10**7)
 
# print("Case #{}: {} {}".format(i, n + m, n * m))
 
 
def iin(): return int(stdin.readline())
def lin(): return list(map(int, stdin.readline().split()))


l=iin()
a=list(input())
n=len(a)
if n<l:
    print('1'+'0'*(l-1))
elif l==n:
    for i in range(l-1,-1,-1):
        chg=int(a[i])
        if chg<9:
            a[i]=str(chg+1)
            break
        else:
            a[i]='0'
    else:
        s1='1'+'0'*(l-1)
        s2=s1*(2)
        print(s2)
        return
    print(*a,sep='')
else:
    if n%l==0:
        x=n//l
        s1=a[:l]
        s2=s1*x
        if s2<=a:
            for i in range(l):
                chg=int(s1[-i-1])
                if chg<9:
                    s1[-i-1]=str(chg+1)
                    break
                else:
                    s1[-i-1]='0'
            else:
                s1='1'+'0'*(l-1)
                s2=s1*(x+1)
                print(s2)
                return
            s2=s1*x
        print(*s2,sep='')

    else:
        x=(n+l-1)//l
        s1='1'+'0'*(l-1)
        s2=s1*x
        print(s2)

