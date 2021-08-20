"""
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
"""
"\ndef main():\n    from sys import stdin,stdout\n    n=int(stdin.readline())\n    for i in range(n+1):\n        stdout.write(' '*(2*(n-i)))\n        for k in range(i+1):\n            if k:\n                if k==1:\n                    stdout.write(' 1 ')\n                else:\n                    stdout.write(str(k)+' ')\n            else:\n                stdout.write('0')\n        for k in range(i-1,-1,-1):\n            if k:\n                stdout.write(str(k)+' ')\n            else:\n                stdout.write('0')\n        stdout.write('')\n    for j in range(i-1,-1,-1):\n        stdout.write(' '*2*(n-j))\n        for k in range(j+1):\n            if k:\n                if k==1:\n                    stdout.write(' 1 ')\n                else:\n                    stdout.write(str(k)+' ')\n            else:\n                stdout.write('0')\n        for k in range(j-1,-1,-1):\n            if k:\n                stdout.write(str(k)+' ')\n            else:\n                stdout.write('0')\n        stdout.write('')\ndef __starting_point():\n    main()\n"
"\ndef main():\n    from sys import stdin,stdout\n    n,m=map(int,stdin.readline().split())\n    mydic={}\n    for _ in range(m):\n        a,b=map(str,stdin.readline().strip().split())\n        mydic[a]=b\n    for k in stdin.readline().strip().split():\n        if len(mydic[k])<len(k):\n            stdout.write(mydic[k]+' ')\n        else:\n            stdout.write(k+' ')\ndef __starting_point():\n    main()\n"
'\ndef main():\n    from sys import stdin,stdout\n    n,m=map(int,stdin.readline().split())\n    k=list(range(1,n+1))\n    a=list(map(int,stdin.readline().split()))\n    while k!=[]:\n        top=k[0]\n        if a[top-1]<=m:\n            k=k[1:]\n            a[top-1]=0\n        else:\n            a[top-1]-=m\n            k=k[1:]+[top]\n    stdout.write(str(top))\ndef __starting_point():\n    main()\n'
"\ndef main():\n    from sys import stdin,stdout\n    n=stdin.readline().strip()\n    i=0\n    k=2\n    t=''\n    for j in n[::-1]:\n        if j=='0':\n            t='0'\n            break\n        elif j=='8':\n            tz='8'\n            break\n        i+=1\n        if k==16:\n            break\n        if int(j+t) & (k-1):\n            continue\n        else:\n            t=j+t\n            k<<=1\n    #print(t,i)\n    if t!='':\n        if int(t)%8==0:\n            if i!=len(n) and t!='0' and t!='8':\n                stdout.write('YES\n'+n[:len(n)-i+1]+t)\n            else:\n                stdout.write('YES\n'+t)\n        else:\n            stdout.write('NO')\n    else:\n        stdout.write('NO')\ndef __starting_point():\n    main()\n"
"\ndef main():\n    from sys import stdin,stdout\n    a=stdin.readline().strip()\n    b=stdin.readline().strip()\n    apc=0\n    anc=0\n    bpc=0\n    bnc=0\n    bqc=0\n    for i in a:\n        if i =='+':\n            apc+=1\n        elif i=='-':\n            anc+=1\n    for i in b:\n        if i=='+':\n            bpc+=1\n        elif i=='-':\n            bnc+=1\n        else:\n            bqc+=1\n    #print(apc,anc,bpc,bnc,bqc)\n    if apc==bpc and anc==bnc and bqc==0:\n        p=1\n    elif bpc>apc or bnc>anc or len(a)!=len(b):\n        p=0\n    else:\n        denom=(1<<bqc)\n        numer=1\n        maxim=max(apc-bpc,anc-bnc)\n        minim=min(aspc-bpc,anc-bnc)\n        while(bqc>maxim):\n            #print(numer)\n            numer*=bqc\n            bqc-=1\n        if minim>1:\n            k=minim\n            while(minim>=2):\n            #print('k',k)\n                k*=(minim-1)\n                minim-=1\n            numer/=k\n        p=numer/denom\n    stdout.write('{:.12f}'.format(p))\ndef __starting_point():\n    main()\n"
"\ndef main():\n    from sys import stdin,stdout\n    for _ in range(int(stdin.readline())):\n        l1,l2,l3,n=stdin.readline().strip().split()\n        L=l1+l2*int(n)+l3\n        n=int(L,2)\n        c=0\n        while n>=0:\n            n=(n&(n+1)) -1\n            #print(n)\n            c+=1\n        stdout.write(str(c)+'\n')\ndef __starting_point():\n    main()\n"
"\ndef main():\n\tfrom sys import stdin,stdout\n\ts=[]\n\tfor i in range(1000000):\n\t\ts.append(True)\n\tfor i in range(2,1000000):\n\t\tif s[i-1]:\n\t\t\tj=2*i\n\t\t\twhile j<=1000000:\n\t\t\t\ts[j-1]=False\n\t\t\t\tj+=i\n\t#print(s[:10])\n\tt=int(stdin.readline())\n\tfor i in stdin.readline().strip().split():\n\t\tn=int(i)\n\t\tk=n**0.5\n\t\tif int(k)==k and s[int(k)-1] and n!=1:\n\t\t\tstdout.write('YES\n')\n\t\telse:\n\t\t\tstdout.write('NO\n')\ndef __starting_point():\n\tmain()\n"
"\ndef main():\n\timport sys\n\ta,b=map(int,sys.stdin.readline().split())\n\tif not a:\n\t\tmaxim='-1'\n\t\tminim='-1'\n\telif not b:\n\t\tif a==1:\n\t\t\tmaxim='0'\n\t\t\tminim='0'\n\t\telse:\n\t\t\tmaxim='-1'\n\t\t\tminim='-1'\n\telse:\n\t\t#finding the maximum number\t\n\t\tmaxim=0\n\t\tn=b\n\t\twhile n:\n\t\t\tif 9>n:\n\t\t\t\tmaxim=maxim*10+n\n\t\t\t\tn=0\n\t\t\telse:\n\t\t\t\tn-=9\n\t\t\t\tmaxim=maxim*10+9\n\t\ts=str(maxim)\n\t\tdiff=a-len(s)\n\t\tif diff<0:\n\t\t\tmaxim='-1'\n\t\telif diff>0:\n\t\t\tmaxim=s+'0'*diff\n\t\telse:\n\t\t\tmaxim=s\n\t\t#finding the minimum number\n\t\tif diff:\n\t\t\tif diff<0:\n\t\t\t\tminim='-1'\n\t\t\telse:\n\t\t\t\ts=maxim[::-1]\n\t\t\t\tfor i in range(len(s)):\n\t\t\t\t\tif int(s[i]):\n\t\t\t\t\t\tbreak\n\t\t\t\t\n\t\t\t\tminim='1'+'0'*(i-1)+str(int(s[i])-1)+s[i+1:]\n\t\telse:\n\t\t\tminim=maxim[::-1]\n\tsys.stdout.write(minim+' '+maxim+'\n')\ndef __starting_point():\n\tmain()\n"
"\ndef main():\t\n\timport sys\n\timport bisect\n\tC=int(1e6)\n\tl=[]\n\tfor i in range(C):\n\t\tl.append(True)\n\tfor i in range(3,C,2):\n\t\tif l[i-1]:\n\t\t\tj=3*i\n\t\t\twhile j<=C:\n\t\t\t\tl[j-1]=False\n\t\t\t\tj+=2*i\n\tfor i in range(3,C,2):\n\t\tl[i]=False\n\tl[0]=False\n\ts=[]\n\tfor i in range(C):\n\t\tif l[i]:\n\t\t\ts.append((i+1)*(i+1))\n\t#print(s[:10])\n\tn=int(sys.stdin.readline())\n\ttup=tuple(map(int,sys.stdin.readline().split()))\n\tfor i in tup:\n\t\tpos=bisect.bisect_left(s,i)\n\t\tif pos!=len(s) and s[pos]==i:\n\t\t\tsys.stdout.write('YES\n')\n\t\telse:\n\t\t\tsys.stdout.write('NO\n')\n\t#print(s[:10])\ndef __starting_point():\n\tmain()\n"
"\ndef main():\n\timport sys\n\tflag=False\n\tminim=10\n\tminindex=-1\n\tmaxindex=-1\n\tn=sys.stdin.readline().strip()\n\tfor i in range(len(n)):\n\t\tif (n[i]=='2' or n[i]=='4' or n[i]=='6' or n[i]=='8'or n[i]=='0') and int(n[i])<=minim:\n\t\t\tif minindex<0:\n\t\t\t\tminindex=i\n\t\t\t\tminim=int(n[i])\n\t\t\t\tflag=True\n\t\t\telse:\n\t\t\t\tmaxindex=i\n\tif flag:\t\n\t\ts=''\n\t\tfor i in range(len(n)):\n\t\t\tif i==minindex:\n\t\t\t\ts+=n[-1]\n\t\t\telif i==len(n)-1:\n\t\t\t\ts+=str(minim)\n\t\t\telse:\n\t\t\t\ts+=n[i]\n\t\tif maxindex>0:\n\t\t\tt=''\n\t\t\tfor i in range(len(n)):\n\t\t\t\tif i==maxindex:\n\t\t\t\t\tt+=n[-1]\n\t\t\t\telif i==len(n)-1:\n\t\t\t\t\tt+=str(minim)\n\t\t\t\telse:\n\t\t\t\t\tt+=n[i]\n\t\t\ts=str(max(int(s),int(t)))\n\telse:\n\t\ts='-1'\n\tsys.stdout.write(s)\ndef __starting_point():\n\tmain()\n"
"\ndef main():\n\timport sys\n\tn=int(sys.stdin.readline())\n\tt=tuple(map(int,sys.stdin.readline().split()))\n\tacc=sum(t)\n\tif acc % 3:\n\t\tsys.stdout.write('0')\n\telse:\n\t\tcnt=[]\n\t\tconst=acc//3\n\t\tss=0\n\t\tfor i in t:\n\t\t\tif acc-ss==const:\n\t\t\t\tcnt.append(1)\n\t\t\telse:\n\t\t\t\tcnt.append(0)\n\t\t\tss+=i \n\t\tfor i in range(n-2,-1,-1):\n\t\t\tcnt[i]+=cnt[i+1];\t\t\n\t\t#print(cnt)\n\t\tans=0\n\t\tss=0\n\t\tfor i in range(n-2):\n\t\t\tss+=t[i]\n\t\t\tif ss==const:\n\t\t\t\tans+=cnt[i+2]\n\t\tsys.stdout.write(str(ans)+'\n')\ndef __starting_point():\n\tmain()\n"


def main():
    from sys import stdin, stdout
    import collections
    stack = collections.deque()
    (n, s, t) = list(map(int, stdin.readline().split()))
    M = tuple(map(int, stdin.readline().split()))
    visited = list((0 for x in range(n)))
    count = 0
    stack.appendleft(s - 1)
    while len(stack):
        top = stack.popleft()
        if top == t - 1:
            break
        elif not visited[M[top] - 1]:
            stack.appendleft(M[top] - 1)
            visited[M[top] - 1] = 1
            count += 1
    if top == t - 1:
        stdout.write(str(count) + '\n')
    else:
        stdout.write('-1\n')


def __starting_point():
    main()


__starting_point()
