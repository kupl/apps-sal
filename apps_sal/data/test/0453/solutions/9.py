from sys import stdin
def main():
    f=stdin.readline().strip()
    x=f.split("+")
    y=x[1].split("=")
    a,b,c=x[0],y[0],y[1]
    if len(a)+len(b)==len(c):
        print(f)
    elif len(a)-1>=1 and len(a)-1 + len(b)==len(c)+1:
        c=c+"|"
        d=[]
        for i in range(len(a)):
                d.append(a[i])
        d.remove(d[i])
        a=''.join(d)
        n=a+'+'+b+'='+c
        print(n)
    elif len(c)-1>=1 and len(a)+1 + len(b) == len(c)-1:
        a=a+"|"
        d=[]
        for i in range(len(c)):
            d.append(c[i])
        d.remove(d[i])
        c=''.join(d)
        n=a+'+'+b+'='+c
        print(n)
    elif len(b)-1>=1 and len(a) + len(b)-1 == len(c)+1:
        c=c+"|"
        d=[]
        for i in range(len(b)):
            d.append(b[i])
        d.remove(d[i])
        b=''.join(d)
        n=a+'+'+b+'='+c
        print(n)
    elif len(c)-1>=0 and len(a)+ len(b)+1 == len(c)-1:
        b=b+"|"
        d=[]
        for i in range(len(c)):
            d.append(c[i])
        d.remove(d[i])
        c=''.join(d)
        n=a+'+'+b+'='+c
        print(n)
    else:
        print("Impossible")
        
main()
