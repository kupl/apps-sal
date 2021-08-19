"""
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
"""
"\ndef main():\n    import sys\n    a,b=map(int,sys.stdin.readline().split())\n    if a>b:\n        if a-b==1:\n            s=''\n            for i in range(a+b):\n                if i&1:\n                    s+='1'\n                else:\n                    s+='0'\n        else:\n            s='-1'\n    elif b>a:\n        if b<=2*(a+1):\n            s=''\n            if b-a==1:\n                for i in range(a+b):\n                    if i&1:\n                        s+='0'\n                    else:\n                        s+='1'\n            else:\n                n=b-a-1\n                i=0\n                flag=0\n                while i<a+b:\n                    if flag&1:\n                        s+='0'\n                    else:\n                        if n:\n                            s+='11'\n                            n-=1\n                            i+=1\n                        else:\n                            s+='1'\n                    i+=1\n                    flag=~flag\n        else:\n            s='-1'\n    else:\n        s=''\n        for i in range(a+b):\n            if i&1:\n                s+='1'\n            else:\n                s+='0'\n    sys.stdout.write(s)\ndef __starting_point():\n    main()\n"
"\ndef main():\n    import sys\n    n=sys.stdin.readline().strip()\n    lodd=int(n[-1])\n    odd=0\n    even=0\n    s=''\n    j=0\n    for i in n:\n        if ord(i)&1:\n            odd+=1\n        else:\n            even+=1\n            feven=int(i)\n            feindex=j\n            if(feven<lodd):\n                break\n        j+=1\n    if even:\n        for i in range(len(n)):\n            if i==feindex:\n                sys.stdout.write(n[-1])\n            elif i==len(n)-1:\n                sys.stdout.write(str(feven))\n            else:\n                sys.stdout.write(n[i])\n    else:\n        sys.stdout.write('-1')\ndef __starting_point():\n    main()\n"
'\ndef main():\n    import sys\n    s=sys.stdin.readline().strip()\n    n=int(sys.stdin.readline())\n    tup=tuple(map(int,sys.stdin.readline().split()))\n    maxim=max(tup)\n    score=0\n    for i in range(len(s)):\n        score+=(i+1)*tup[ord(s[i])-97]\n    d=n*(2*len(s)+n+1)//2\n    score+=maxim*d\n    sys.stdout.write(str(score))\ndef __starting_point():\n    main()\n'
"\ndef main():\n    from sys import stdin,stdout\n    from math import ceil,sqrt\n    def sqr(a):\n        return a*a\n    r,x,y,a,b=map(int,stdin.readline().split())\n    mid=((x+a)/2,(y+b)/2)\n    #print(mid)\n    dis=sqrt(sqr(x-mid[0])+sqr(y-mid[1]))\n    #print(dis)\n    n=ceil(dis/r)\n    stdout.write(str(n)+'\n')\ndef __starting_point():\n    main()\n"
"\ndef main():\n    from sys import stdin,stdout\n    n=int(stdin.readline())\n    tup=tuple(map(int,stdin.readline().split()))\n    minim=min(tup)\n    maxim=max(tup)\n    maximindex=tup.index(maxim)\n    flag=1\n    i=0\n    pv=tup[-1]\n    while i<n:\n        if tup[i]<pv:\n            if tup[i]==minim and pv==maxim:\n                l=i+1\n                while l<max(maximindex,n):\n                    if tup[l]<tup[l-1]:\n                        flag=0\n                        break\n                    l+=1\n                break\n            else:\n                flag=0\n                break\n        pv=tup[i]\n        i+=1\n    #print(i)\n    if flag:\n        if i:\n            stdout.write(str(n-i))\n        else:\n            stdout.write('0')\n    else:\n        stdout.write('-1')\ndef __starting_point():\n    main()\n"
'\ndef main():\n    from sys import stdin,stdout\n    MOD=int(1e9)+7\n    x,y=map(int,stdin.readline().split())\n    n=(int(stdin.readline())-1)%6\n    tup=(x,y,y-x,-x,-y,x-y)\n    stdout.write(str(tup[n]%MOD))\ndef __starting_point():\n    main()\n'
'\ndef main():\n    from sys import stdin,stdout\n    n=int(stdin.readline())\n    ksum=n\n    for i in range(n):\n        x=int(stdin.readline())\n        if i:\n            if x<p:\n                ksum+=1+(p-x)\n                p=x\n            else:\n                ksum+=(1+x-p)\n                p=x\n        else:\n            ksum+=x\n            p=x\n    stdout.write(str(ksum))\ndef __starting_point():\n    main()\n'
"\ndef main():\n    from sys import stdin,stdout\n    import collections\n    s=stdin.readline().strip()\n    t=stdin.readline().strip()\n    if set(t).issubset(set(s)) and len(t)<=len(s):\n        sp=0\n        tp=0\n        sc=collections.Counter(s)\n        tc=collections.Counter(t)\n        while sp<len(s) and tp<len(t):\n            if s[sp]==t[tp]:\n                tp+=1\n                sp+=1\n            else:\n                sp+=1\n        if tp==len(t):\n            stdout.write('automaton')\n        else:\n            if len(t)==len(s):\n                if sc!=tc:\n                    stdout.write('need tree')\n                else:\n                    stdout.write('array')\n            else:\n                flag=1\n                for i in sc:\n                    if sc[i]<tc[i]:\n                        flag=0\n                if flag:\n                    stdout.write('both')\n                else:\n                    stdout.write('need tree')\n    else:\n        stdout.write('need tree')\ndef __starting_point():\n    main()\n"
'\ndef main():\n    from sys import stdin,stdout\n    import collections\n    myDic=collections.defaultdict(set)\n    for _ in range(int(stdin.readline())):\n        a,b=map(int,stdin.readline().split())\n        myDic[a].add(b)\n    index=max(myDic[min(myDic)])\n    for i in sorted(myDic):\n        if max(myDic[i])<index:\n            index=i\n        else:\n            index=max(myDic[i])\n    stdout.write(str(index))\n    \ndef __starting_point():\n    main()\n'
'\ndef main():\n    from sys import stdin,stdout\n    import collections\n    n=int(stdin.readline())\n    tup=tuple(map(int,stdin.readline().split()))\n    maxim=max(tup)\n    cnt=collections.Counter(tup)\n    f=[0,cnt[1]]\n    for i in range(2,maxim+1):\n        f.append(max(f[i-1],f[i-2]+cnt[i]*i))\n    stdout.write(str(f[maxim]))\ndef __starting_point():\n    main()\n'
'\ndef main():\n    from sys import stdin,stdout\n    n,k,l,c,d,p,nl,np=map(int,stdin.readline().split())\n    stdout.write(str(min((k*l//nl,c*d,p//np))//n))\ndef __starting_point():\n    main()\n'
"\ndef main():\n    from sys import stdin,stdout\n    s=stdin.readline().strip()\n    tup=()\n    for _ in range(int(stdin.readline())):\n        a,b=map(int,stdin.readline().split())\n        counter=0\n        for i in range(a-1,b-1):\n            if s[i]==s[i+1]:\n                counter+=1\n        tup+=(counter,)\n    for i in tup:\n        stdout.write(str(i)+'\n')\ndef __starting_point():\n    main()\n"


def main():
    from sys import stdin, stdout
    (x, a, b) = list(map(int, stdin.readline().split()))
    (c, y, d) = list(map(int, stdin.readline().split()))
    (e, f, z) = list(map(int, stdin.readline().split()))
    x = (2 * b + d - c) // 2
    z = b + e - x
    y = x + c + e - f - a
    stdout.write(str(x) + ' ' + str(a) + ' ' + str(b) + '\n')
    stdout.write(str(c) + ' ' + str(y) + ' ' + str(d) + '\n')
    stdout.write(str(e) + ' ' + str(f) + ' ' + str(z))


def __starting_point():
    main()


__starting_point()
