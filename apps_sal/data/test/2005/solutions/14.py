'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
def __starting_point():
    main()
'''
#372
#1
'''
def main():
    from sys import stdin,stdout
    n,c=map(int,stdin.readline().split())
    tup=tuple(map(int,stdin.readline().split()))
    counter=1
    for i in range(1,n):
        if tup[i]-tup[i-1]<=c:
            counter+=1
        else:
            counter=1
    stdout.write(str(counter))
def __starting_point():
    main()
'''
#2
'''
def main():
    from sys import stdin,stdout
    s=stdin.readline().strip().lower()
    dic={}
    qcounter=0
    for i in 'qwertyuiopasdfghjklzxcvbnm':
        dic[i]=0
    if len(s)<26:
        stdout.write('-1')
    else:
        for i in s:
            if i=='?':
                qcounter+=1
            else:
                dic[i]+=1
        l=[]
        x=list(dic.values()).count(0)
        if qcounter==26 and x==26:
            stdout.write('qwertyuiopasdfghjklzxcvbnm'.upper())
        elif x==0 and qcounter==0:
            stdout.write(s.upper())
        elif qcounter>=x:
            for i in 'qwertyuiopasdfghjklzxcvbnm':
                if dic[i]==0:
                    l.append(i.upper())
            m=len(l)
            i=0
            t=''
            for j in range(len(s)):
                if s[j]=='?':
                    if i>=m:
                        i=0
                    t=t[:j]+l[i]
                    i+=1
                else:
                    t+=s[j].upper()
            stdout.write(t)
        else:
            stdout.write('-1')
def __starting_point():
    main()
'''
#373
#1
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    tup=tuple(map(int,stdin.readline().split()))
    if n==1:
        if tup[0]==0:
            stdout.write('UP')
        elif tup[0]==15:
            stdout.write('DOWN')
        else:
            stdout.write('-1')
    else:
        if tup[-1]-tup[-2]>0:
            if tup[-1]==15:
                stdout.write('DOWN')
            else:
                stdout.write('UP')
        else:
            if tup[-1]==0:
                stdout.write('UP')
            else:
                stdout.write('DOWN')
def __starting_point():
    main()
'''
#2
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    s=stdin.readline().strip()
    rcount=s.count('r')
    bcount=s.count('b')
    #print(rcount,bcount)
    if n&1:
        count=0
        if abs(rcount-bcount)==1:
            if rcount>bcount:
                for i in s[::2]:
                    if i!='r':
                        count+=1
            else:
                for i in s[::2]:
                    if i!='b':
                        count+=1
        else:
            mid=n//2+1
            xtra=max(rcount,bcount)-mid
            if rcount>bcount:
                 for i in s[::2]:
                    if i!='r':
                        count+=1
            else:
                 for i in s[::2]:
                    if i!='b':
                        count+=1
            count+=xtra
    else:
        count=0
        if bcount==rcount:
            if s[0]=='r':
                for i in s[::2]:
                    if i!='r':
                        count+=1
            else:
                for i in s[::2]:
                    if i!='b':
                        count+=1
        else:
            count=abs(bcount-acount)
    stdout.write(str(count))
def __starting_point():
    main()
'''
#3
'''
def main():
    from sys import stdin,stdout
    n,t=map(int,stdin.readline().split())
    s=stdin.readline().strip()
    d=s.index('.')
    p=s
    #print(p,s,d)
    for _ in range(t):
        n=len(s)
        #print(n)
        for i in range(d+1,n):
            #print(i)
            if int(s[i])>=5:
                if i-1==d:
                    t=int(s[i-2])+1
                    s=s[:i-2]+str(t)
                    break
                else:
                    t=int(s[i-1])+1
                    s=s[:i-1]+str(t)
                    break
        if p==s:
            break
        else:
            p=s
    stdout.write(s)
def __starting_point():
    main()
'''
#ENCODE 16.1
#1
'''
def main():
    from sys import stdin,stdout
    for _ in range(int(stdin.readline())):
        s='pikachu'
        t=stdin.readline().strip()
        for i in t:
            if len(s)==0:
                break
            if i in s:
                s=s.replace(i,'')
        if(len(s)):
            stdout.write('NO\n')
        else:
            stdout.write('YES\n')
def __starting_point():
    main()
'''
#2
'''
def main():
    from sys import stdin,stdout
    for _ in range(int(stdin.readline())):
        n=int(stdin.readline())
        n=n*(n+1)*(2*n+1)
        n//=6
        stdout.write(str(n)+'\n')
def __starting_point():
    main()
'''
#5
'''
def main():
    def gcd(a,b):
        if b:
            return gcd(b,a%b)
        else:
            return a
    from sys import stdin,stdout
    n,q=map(int,stdin.readline().split())
    tup=tuple(map(int,stdin.readline().split()))
    for _ in range(q):
        c=0
        i=int(stdin.readline())
        if i!=1:
            for k in range(i-1):
                if gcd(tup[k],tup[i-1])!=1:
                    c+=1
        if c:
            stdout.write(str(c)+'\n')
        else:
            stdout.write('-1\n')
def __starting_point():
    main()
'''
#374
#1
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    s=stdin.readline().strip().lower()
    l=[]
    counter=0
    for i in range(n):
        if s[i]=='b':
            counter+=1
        else:
            if counter:
                l.append(counter)
                counter=0
    if counter:
        l.append(counter)
    if len(l):
        stdout.write(str(len(l))+'\n')
        for i in l:
            stdout.write(str(i)+' ')
    else:
        stdout.write('0')
def __starting_point():
    main()
'''
#2
'''
def main():
    from sys import stdin,stdout
    n,k=map(int,stdin.readline().split())
    p=[]
    for _ in range(n):
        p.append(stdin.readline().strip())
    p.sort(key=len)
    P=stdin.readline().strip()
    j=0
    count=0
    for i in p:
        j+=1
        if len(i)==len(P):
            count+=1
            minim=count
            break
        else:
            count+=1
            if j%k==0:
                count+=5
    count=0
    j=0
    for i in p:
        j+=1
        if len(i)>len(P):
            if (j-1)%k==0:
                count-=5
            maxim=count
            break
        else:
            if i==p[-1]:
                maxim=count+1
                break
            else:
                count+=1
                #print(count,end=', ')
                if j%k==0:
                    count+=5
                #print(count)
    stdout.write(str(minim)+' '+str(maxim))
def __starting_point():
    main()
'''
#375
#1
'''
def main():
    from sys import stdin,stdout
    x,y,z=map(int,stdin.readline().split())
    minim=min(x,y,z)
    maxim=max(x,y,z)
    minimum=-1
    for i in range(minim,maxim+1):
        if minimum<0:
            minimum=abs(i-x)+abs(i-y)+abs(i-z)
        else:
            minimum=min(minimum,abs(i-x)+abs(i-y)+abs(i-z))
    stdout.write(str(minimum))
def __starting_point():
    main()
'''
#2
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    s=stdin.readline()
    bra=[]
    line=set()
    w=''
    braketflag=False
    for i in s:
        if i=='_':
            if w!='':
                if not braketflag:
                    line.add(w)
                else:
                    bra.append(w)
            w=''
        elif i=='(':
            braketflag=True
            if w!='':
                line.add(w)
            w=''
        elif i==')':
            braketflag=False
            if w!='':
                bra.append(w)
            w=''
        elif i=='\n':
            if w!='':
                line.add(w)
        else:
            w+=i
    maxi=0
    for i in line:
        maxi=max(maxi,len(i))
    stdout.write(str(maxi)+' '+str(len(bra)))
def __starting_point():
    main()
'''
'''
#3
def main():
    from sys import stdin,stdout
    n,m=map(int,stdin.readline().split())
    l=list(map(int,stdin.readline().split()))
    dic={}
    for j in range(1,m+1):
        dic[j]=0
    for i in l:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    eq=n//m
    c=0
    for j in range(1,m+1):
        if dic[j]<eq:
            break
    i=0
    while i<n:
        if l[i]>m:
            if dic[j]<eq:
                l[i]=j
                dic[j]+=1
                c+=1
                i+=1
            else:
                j+=1
                if j>m:
                    break
        else:
            i+=1
    flag=True
    for j in range(1,m+1):
        if dic[j]<eq:
            flag=False
            break
    if flag:
        stdout.write(str(eq)+' '+str(c)+'\n')
        for i in l:
            stdout.write(str(i)+' ')
    else:
        i=0
        while(i<n):
            if dic[l[i]]>eq:
                if j<=m and dic[j]<eq:
                    l[i]=j
                    dic[j]+=1
                    c+=1
                elif j<=m:
                    j+=1
                else:
                    break
            i+=1
        stdout.write(str(eq)+' '+str(c)+'\n')
        for i in l:
            stdout.write(str(i)+' ')
def __starting_point():
    main()
'''
#377
#1
'''
def main():
    from sys import stdin,stdout
    k,r=map(int,stdin.readline().split())
    rem=k%10
    if rem:
        if rem==r:
            stdout.write('1')
        else:
            if rem ==5:
                a=2
            elif rem == 2:
                a=5
            else:
                a=11
            for i in range(1,10):
                if (rem*i) %10==r:
                    break
            stdout.write(str(min(a,i)))
    else:
        stdout.write('0')
def __starting_point():
    main()
'''
#2
'''
def main():
    from sys import stdin,stdout
    n,k=map(int,stdin.readline().split())
    t=tuple(map(int,stdin.readline().split()))
    l=[]
    c=0
    l+=[t[0]]
    for i in range(1,n):
        s=l[i-1]+t[i]
        if s<k:
            c+=(k-s)
            l.append(t[i]+(k-s))
        else:
            l.append(t[i])
    stdout.write(str(c)+'\n')
    for i in l:
        stdout.write(str(i)+' ')
def __starting_point():
    main()
'''
#1
'''
def main():
    from sys import stdin,stdout
    for _ in range(int(stdin.readline())):
        m1,m2,m3=map(int,stdin.readline().split())
        o1,o2,o3=map(int,stdin.readline().split())
        p1,p2,p3=map(int,stdin.readline().split())
        t=(sum((m1,m2,m3)),sum((o1,o2,o3)),sum((p1,p2,p3)),sum((m1,o1,p1)),sum((m2,o2,p2)),sum((m3,o3,p3)))
        s=max(filter(lambda x: x&1 ,t))
        stdout.write(str(s)+'\n')
def __starting_point():
    main()
'''
#378
#1
'''
def main():
    from sys import stdin,stdout
    s=stdin.readline().lower()
    maxjump=0
    j=1
    for i in s:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y' or i=='\n':
            maxjump=max(maxjump,j)
            j=1
        else:
            j+=1
    stdout.write(str(maxjump))
def __starting_point():
    main()
'''
#2
'''
def main():
    from sys import stdin,stdout
    c=[]
    for _ in range(int(stdin.readline())):
        l,r=map(int,stdin.readline().split())
        c.append(l-r)
    flag=1
    for i in c:
        if i<0:
            flag=0
            break
    if flag:
        stdout.write('0')
    else:
        flag=2
        for i in c:
            if i>0:
                flag=0
                break
        if flag:
            stdout.write('0')
        else:
            index=1
            csum=sum(c)
            msum=csum
            for i in range(len(c)):
                nsum=abs(csum-c[i]*(-2))
                if nsum > msum:
                    index=i+1
                    msum=nsum
            stdout.write(str(index))
def __starting_point():
    main()
'''
#NOVEMBER LONG 2016
#ALEXTASK
'''
def main():
    from sys import stdin,stdout
    from fractions import gcd
    for _ in range(int(stdin.readline())):
        n=int(stdin.readline())
        tup=tuple(map(int,stdin.readline().split()))
        lcm=(tup[0]*tup[1])//gcd(tup[0],tup[1])
        for x in range(len(tup)):
            for y in range(len(tup)):
                if y>x:
                    lcm=min(lcm,(tup[x]*tup[y])//gcd(tup[x],tup[y]))
        stdout.write(str(lcm)+'\n')
def __starting_point():
    main()
'''
#CPERM
'''
def main():
    from sys import stdin,stdout
    MOD=int(1e9)+7
    def power(a,b):
        if b==0:
            return 1
        if b & 1:
            return (a*power(a,b-1))%MOD
        else:
            return power((a*a)%MOD,b>>1)%MOD
    for _ in range(int(stdin.readline())):
        n=int(stdin.readline())
        n-=2
        if n>0:
            n=((power(2,n)-1)%MOD<<1)%MOD
        else:
            n=0
        stdout.write(str(n)+'\n')
def __starting_point():
    main()
'''
#CHSQR
'''
def main():
    from sys import stdin,stdout
    for _ in range(int(stdin.readline())):
        n=int(stdin.readline())
        #arr=list(list(0 for x in range(n)) for x in range(n))
        l=[]
        i=0
        j=2
        while i<n-1:
            if j > n:
                j=n-2
            l.append(n-j)
            if j&1:
                j-=2
            else:
                j+=2
            i+=1
        l+=([n]+l)
        #print(l)
        for i in range(n):
            for j in range(n):
                stdout.write(str(l[i+j])+' ')
            stdout.write('\n')
def __starting_point():
    main()
'''
#URBANDEV
'''
def main():
    from sys import stdin,stdout
    h=[]
    v=[]
    order=[]
    n=int(stdin.readline())
    for i in range(n):
        a,b,x,y=map(int,stdin.readline().split())
        if a-x:
            h.append((min(a,x),max(a,x),y))
            order.append(1)
        else:
            v.append((min(y,b),max(y,b),x))
            order.append(0)
    #print(l,r)
    hd=list(0 for x in range(len(h)))
    vd=list(0 for x in range(len(v)))
    lightcounter=0
    for i in range(len(v)):
        for j in range(len(h)):
            y=h[j][2]
            x=v[i][2]
            miny=v[i][0]
            maxy=v[i][1]
            minx=h[j][0]
            maxx=h[j][1]
            if y>miny and y<maxy and x>minx and x<maxx:
                lightcounter+=1
                hd[j]+=1
                vd[i]+=1
            elif x==minx:
                if y>miny and y<maxy:
                    lightcounter+=1
                    hd[j]+=1
                    vd[i]+=1
            elif x==maxx:
                if y>miny and y<maxy:
                    lightcounter+=1
                    hd[j]+=1
                    vd[i]+=1
            elif miny==y:
                if x>minx and x<maxx:
                    lightcounter+=1
                    hd[j]+=1
                    vd[i]+=1
            elif maxy==y:
                if x>minx and x<maxx:
                    lightcounter+=1
                    hd[j]+=1
                    vd[i]+=1
    stdout.write(str(lightcounter)+'\n')
    for i in range(n):
        if order[i]:
            stdout.write(str(hd[0])+' ')
            hd=hd[1:]
        else:
            stdout.write(str(vd[0])+' ')
            vd=vd[1:]
def __starting_point():
    main()
'''
#FRIEMEET
'''
from collections import *
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes: 
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def main():
    from sys import stdin,stdout
    from fractions import Fraction
    for _ in range(int(stdin.readline())):
        G=Graph()
        n,m=map(int,stdin.readline().split())
        for x in range(1,n+1):
            G.add_node(x)
        for _ in range(n-1):
            a,b,l=map(int,stdin.readline().split())
            G.add_edge(a,b,l)
        l=tuple(map(int,stdin.readline().split()))
        ksum=0
        for i in range(len(l)-1):
            d,p=dijsktra(G,l[i])
            for j in range(i+1,len(l)):
                ksum+=d[l[j]]*2
        ans=Fraction(ksum,m*m)
        stdout.write(str(ans.numerator)+' '+str(ans.denominator)+'\n')
def __starting_point():
    main()
'''
#734A
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    s=stdin.readline().strip()
    dcount=s.count('D')
    acount=s.count('A')
    if dcount>acount:
        stdout.write('Danik')
    elif dcount<acount:
        stdout.write('Anton')
    else:
        stdout.write('Friendship')
def __starting_point():
    main()
'''
#734B
'''
def main():
    from sys import stdin,stdout
    a,b,c,d=map(int,stdin.readline().split())
    min256=min(a,c,d)
    ksum=256*min256
    a-=min256
    min32=min(a,b)
    ksum+=min32*32
    stdout.write(str(ksum))
def __starting_point():
    main()
'''
#381
#A
'''
def main():
    from sys import stdin,stdout
    n,a,b,c=map(int,stdin.readline().split())
    rem=n%4
    if rem:
        if rem & 1:
            if rem==1:
                minim=min((3*a,c,b+a))
                stdout.write(str(minim))
            else:
                minim=min(a,c+b)
                stdout.write(str(minim))
        else:
            minim=min((b,2*a,2*c))
            stdout.write(str(minim))
    else:
        stdout.write('0')
def __starting_point():
    main()
'''
#B
'''
def main():
    from sys import stdin,stdout
    n,m=map(int,stdin.readline().split())
    t=tuple(map(int,stdin.readline().split()))
    maxim=0
    for i in range(m):
        l,r=map(int,stdin.readline().split())
        s=sum(t[l-1:r])
        if s>0:
            maxim+=s
    stdout.write(str(maxim))
def __starting_point():
    main()
'''
#C
'''
def main():
    from sys import stdin,stdout
    n,m=map(int,stdin.readline().split())
    minim=n
    a=list(n for x in range(n))
    #print(a)
    for i in range(m):
        l,r=map(int,stdin.readline().split())
        if r-l < minim:
            minim=r-l
            minimpair=(l-1,r)
    a[minimpair[0]:minimpair[1]]=list(i for i in range(minim+1))
    stdout.write(str(minim+1)+'\n')
    for i in a:
        stdout.write(str(i)+' ')
def __starting_point():
    main()
'''
'''
#L42
#1
def main():
    from sys import stdin,stdout
    for _ in range(int(stdin.readline())):
        s=stdin.readline().strip()
        t=''
        for i in s:
            if i=='<':
                t+='>'
            elif i=='>':
                t+='<'
            else:
                t+=i
        stdout.write(str(t.count('><'))+'\n')
def __starting_point():
    main()
'''
#382
#1
'''
def main():
    from sys import stdin,stdout
    n,k=map(int,stdin.readline().split())
    s=stdin.readline().strip()
    g=s.index('G')
    t=s.index('T')
    if abs(t-g)%k:
        stdout.write('NO')
    else:
        minim=min(t,g)
        maxim=max(t,g)
        flag=1
        while minim<maxim:
            if s[minim]=='#':
                flag=0
                break
            minim+=k
        if flag:
            stdout.write('YES')
        else:
            stdout.write('NO')
def __starting_point():
    main()
'''
#2
def main():
    from sys import stdin,stdout
    import collections
    n,n1,n2=list(map(int,stdin.readline().split()))
    a=sorted(map(int,stdin.readline().split()),reverse=True)
    minim=min(n1,n2)
    maxim=max(n1,n2)
    ans=sum(a[:minim])/minim
    #print(ans)
    ans+=sum(a[minim:minim+maxim])/maxim
    #print(ans)
    stdout.write('{:.6f}'.format(ans))
def __starting_point():
    main()

__starting_point()
