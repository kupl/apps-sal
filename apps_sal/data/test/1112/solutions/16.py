'''
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
'''
'''
def main():
    import sys
    a,b=map(int,sys.stdin.readline().split())
    if a>b:
        if a-b==1:
            s=''
            for i in range(a+b):
                if i&1:
                    s+='1'
                else:
                    s+='0'
        else:
            s='-1'
    elif b>a:
        if b<=2*(a+1):
            s=''
            if b-a==1:
                for i in range(a+b):
                    if i&1:
                        s+='0'
                    else:
                        s+='1'
            else:
                n=b-a-1
                i=0
                flag=0
                while i<a+b:
                    if flag&1:
                        s+='0'
                    else:
                        if n:
                            s+='11'
                            n-=1
                            i+=1
                        else:
                            s+='1'
                    i+=1
                    flag=~flag
        else:
            s='-1'
    else:
        s=''
        for i in range(a+b):
            if i&1:
                s+='1'
            else:
                s+='0'
    sys.stdout.write(s)
def __starting_point():
    main()
'''
'''
def main():
    import sys
    n=sys.stdin.readline().strip()
    lodd=int(n[-1])
    odd=0
    even=0
    s=''
    j=0
    for i in n:
        if ord(i)&1:
            odd+=1
        else:
            even+=1
            feven=int(i)
            feindex=j
            if(feven<lodd):
                break
        j+=1
    if even:
        for i in range(len(n)):
            if i==feindex:
                sys.stdout.write(n[-1])
            elif i==len(n)-1:
                sys.stdout.write(str(feven))
            else:
                sys.stdout.write(n[i])
    else:
        sys.stdout.write('-1')
def __starting_point():
    main()
'''
'''
def main():
    import sys
    s=sys.stdin.readline().strip()
    n=int(sys.stdin.readline())
    tup=tuple(map(int,sys.stdin.readline().split()))
    maxim=max(tup)
    score=0
    for i in range(len(s)):
        score+=(i+1)*tup[ord(s[i])-97]
    d=n*(2*len(s)+n+1)//2
    score+=maxim*d
    sys.stdout.write(str(score))
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    from math import ceil,sqrt
    def sqr(a):
        return a*a
    r,x,y,a,b=map(int,stdin.readline().split())
    mid=((x+a)/2,(y+b)/2)
    dis=sqrt(sqr(x-mid[0])+sqr(y-mid[1]))
    n=ceil(dis/r)
    stdout.write(str(n)+'\n')
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    tup=tuple(map(int,stdin.readline().split()))
    minim=min(tup)
    maxim=max(tup)
    maximindex=tup.index(maxim)
    flag=1
    i=0
    pv=tup[-1]
    while i<n:
        if tup[i]<pv:
            if tup[i]==minim and pv==maxim:
                l=i+1
                while l<max(maximindex,n):
                    if tup[l]<tup[l-1]:
                        flag=0
                        break
                    l+=1
                break
            else:
                flag=0
                break
        pv=tup[i]
        i+=1
    if flag:
        if i:
            stdout.write(str(n-i))
        else:
            stdout.write('0')
    else:
        stdout.write('-1')
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    MOD=int(1e9)+7
    x,y=map(int,stdin.readline().split())
    n=(int(stdin.readline())-1)%6
    tup=(x,y,y-x,-x,-y,x-y)
    stdout.write(str(tup[n]%MOD))
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    ksum=n
    for i in range(n):
        x=int(stdin.readline())
        if i:
            if x<p:
                ksum+=1+(p-x)
                p=x
            else:
                ksum+=(1+x-p)
                p=x
        else:
            ksum+=x
            p=x
    stdout.write(str(ksum))
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    import collections
    s=stdin.readline().strip()
    t=stdin.readline().strip()
    if set(t).issubset(set(s)) and len(t)<=len(s):
        sp=0
        tp=0
        sc=collections.Counter(s)
        tc=collections.Counter(t)
        while sp<len(s) and tp<len(t):
            if s[sp]==t[tp]:
                tp+=1
                sp+=1
            else:
                sp+=1
        if tp==len(t):
            stdout.write('automaton')
        else:
            if len(t)==len(s):
                if sc!=tc:
                    stdout.write('need tree')
                else:
                    stdout.write('array')
            else:
                flag=1
                for i in sc:
                    if sc[i]<tc[i]:
                        flag=0
                if flag:
                    stdout.write('both')
                else:
                    stdout.write('need tree')
    else:
        stdout.write('need tree')
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    import collections
    myDic=collections.defaultdict(set)
    for _ in range(int(stdin.readline())):
        a,b=map(int,stdin.readline().split())
        myDic[a].add(b)
    index=max(myDic[min(myDic)])
    for i in sorted(myDic):
        if max(myDic[i])<index:
            index=i
        else:
            index=max(myDic[i])
    stdout.write(str(index))
    
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    import collections
    n=int(stdin.readline())
    tup=tuple(map(int,stdin.readline().split()))
    maxim=max(tup)
    cnt=collections.Counter(tup)
    f=[0,cnt[1]]
    for i in range(2,maxim+1):
        f.append(max(f[i-1],f[i-2]+cnt[i]*i))
    stdout.write(str(f[maxim]))
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    n,k,l,c,d,p,nl,np=map(int,stdin.readline().split())
    stdout.write(str(min((k*l//nl,c*d,p//np))//n))
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    s=stdin.readline().strip()
    tup=()
    for _ in range(int(stdin.readline())):
        a,b=map(int,stdin.readline().split())
        counter=0
        for i in range(a-1,b-1):
            if s[i]==s[i+1]:
                counter+=1
        tup+=(counter,)
    for i in tup:
        stdout.write(str(i)+'\n')
def __starting_point():
    main()
'''


def main():
    from sys import stdin, stdout
    x, a, b = list(map(int, stdin.readline().split()))
    c, y, d = list(map(int, stdin.readline().split()))
    e, f, z = list(map(int, stdin.readline().split()))
    x = (2 * b + d - c) // 2
    z = b + e - x
    y = x + c + e - f - a
    stdout.write(str(x) + ' ' + str(a) + ' ' + str(b) + '\n')
    stdout.write(str(c) + ' ' + str(y) + ' ' + str(d) + '\n')
    stdout.write(str(e) + ' ' + str(f) + ' ' + str(z))


def __starting_point():
    main()


__starting_point()
