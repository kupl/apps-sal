'''
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
'''
#118B
'''
def main():
    from sys import stdin,stdout
    n=int(stdin.readline())
    for i in range(n+1):
        stdout.write(' '*(2*(n-i)))
        for k in range(i+1):
            if k:
                if k==1:
                    stdout.write(' 1 ')
                else:
                    stdout.write(str(k)+' ')
            else:
                stdout.write('0')
        for k in range(i-1,-1,-1):
            if k:
                stdout.write(str(k)+' ')
            else:
                stdout.write('0')
        stdout.write('')
    for j in range(i-1,-1,-1):
        stdout.write(' '*2*(n-j))
        for k in range(j+1):
            if k:
                if k==1:
                    stdout.write(' 1 ')
                else:
                    stdout.write(str(k)+' ')
            else:
                stdout.write('0')
        for k in range(j-1,-1,-1):
            if k:
                stdout.write(str(k)+' ')
            else:
                stdout.write('0')
        stdout.write('')
def __starting_point():
    main()
'''
#499B
'''
def main():
    from sys import stdin,stdout
    n,m=map(int,stdin.readline().split())
    mydic={}
    for _ in range(m):
        a,b=map(str,stdin.readline().strip().split())
        mydic[a]=b
    for k in stdin.readline().strip().split():
        if len(mydic[k])<len(k):
            stdout.write(mydic[k]+' ')
        else:
            stdout.write(k+' ')
def __starting_point():
    main()
'''
#450A
'''
def main():
    from sys import stdin,stdout
    n,m=map(int,stdin.readline().split())
    k=list(range(1,n+1))
    a=list(map(int,stdin.readline().split()))
    while k!=[]:
        top=k[0]
        if a[top-1]<=m:
            k=k[1:]
            a[top-1]=0
        else:
            a[top-1]-=m
            k=k[1:]+[top]
    stdout.write(str(top))
def __starting_point():
    main()
'''
#550C
'''
def main():
    from sys import stdin,stdout
    n=stdin.readline().strip()
    i=0
    k=2
    t=''
    for j in n[::-1]:
        if j=='0':
            t='0'
            break
        elif j=='8':
            tz='8'
            break
        i+=1
        if k==16:
            break
        if int(j+t) & (k-1):
            continue
        else:
            t=j+t
            k<<=1
    #print(t,i)
    if t!='':
        if int(t)%8==0:
            if i!=len(n) and t!='0' and t!='8':
                stdout.write('YES\n'+n[:len(n)-i+1]+t)
            else:
                stdout.write('YES\n'+t)
        else:
            stdout.write('NO')
    else:
        stdout.write('NO')
def __starting_point():
    main()
'''
#476B
'''
def main():
    from sys import stdin,stdout
    a=stdin.readline().strip()
    b=stdin.readline().strip()
    apc=0
    anc=0
    bpc=0
    bnc=0
    bqc=0
    for i in a:
        if i =='+':
            apc+=1
        elif i=='-':
            anc+=1
    for i in b:
        if i=='+':
            bpc+=1
        elif i=='-':
            bnc+=1
        else:
            bqc+=1
    #print(apc,anc,bpc,bnc,bqc)
    if apc==bpc and anc==bnc and bqc==0:
        p=1
    elif bpc>apc or bnc>anc or len(a)!=len(b):
        p=0
    else:
        denom=(1<<bqc)
        numer=1
        maxim=max(apc-bpc,anc-bnc)
        minim=min(aspc-bpc,anc-bnc)
        while(bqc>maxim):
            #print(numer)
            numer*=bqc
            bqc-=1
        if minim>1:
            k=minim
            while(minim>=2):
            #print('k',k)
                k*=(minim-1)
                minim-=1
            numer/=k
        p=numer/denom
    stdout.write('{:.12f}'.format(p))
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    for _ in range(int(stdin.readline())):
        l1,l2,l3,n=stdin.readline().strip().split()
        L=l1+l2*int(n)+l3
        n=int(L,2)
        c=0
        while n>=0:
            n=(n&(n+1)) -1
            #print(n)
            c+=1
        stdout.write(str(c)+'\n')
def __starting_point():
    main()
'''
#230B
'''
def main():
	from sys import stdin,stdout
	s=[]
	for i in range(1000000):
		s.append(True)
	for i in range(2,1000000):
		if s[i-1]:
			j=2*i
			while j<=1000000:
				s[j-1]=False
				j+=i
	#print(s[:10])
	t=int(stdin.readline())
	for i in stdin.readline().strip().split():
		n=int(i)
		k=n**0.5
		if int(k)==k and s[int(k)-1] and n!=1:
			stdout.write('YES\n')
		else:
			stdout.write('NO\n')
def __starting_point():
	main()
'''
#489C
'''
def main():
	import sys
	a,b=map(int,sys.stdin.readline().split())
	if not a:
		maxim='-1'
		minim='-1'
	elif not b:
		if a==1:
			maxim='0'
			minim='0'
		else:
			maxim='-1'
			minim='-1'
	else:
		#finding the maximum number	
		maxim=0
		n=b
		while n:
			if 9>n:
				maxim=maxim*10+n
				n=0
			else:
				n-=9
				maxim=maxim*10+9
		s=str(maxim)
		diff=a-len(s)
		if diff<0:
			maxim='-1'
		elif diff>0:
			maxim=s+'0'*diff
		else:
			maxim=s
		#finding the minimum number
		if diff:
			if diff<0:
				minim='-1'
			else:
				s=maxim[::-1]
				for i in range(len(s)):
					if int(s[i]):
						break
				
				minim='1'+'0'*(i-1)+str(int(s[i])-1)+s[i+1:]
		else:
			minim=maxim[::-1]
	sys.stdout.write(minim+' '+maxim+'\n')
def __starting_point():
	main()
'''
#230B
'''
def main():	
	import sys
	import bisect
	C=int(1e6)
	l=[]
	for i in range(C):
		l.append(True)
	for i in range(3,C,2):
		if l[i-1]:
			j=3*i
			while j<=C:
				l[j-1]=False
				j+=2*i
	for i in range(3,C,2):
		l[i]=False
	l[0]=False
	s=[]
	for i in range(C):
		if l[i]:
			s.append((i+1)*(i+1))
	#print(s[:10])
	n=int(sys.stdin.readline())
	tup=tuple(map(int,sys.stdin.readline().split()))
	for i in tup:
		pos=bisect.bisect_left(s,i)
		if pos!=len(s) and s[pos]==i:
			sys.stdout.write('YES\n')
		else:
			sys.stdout.write('NO\n')
	#print(s[:10])
def __starting_point():
	main()
'''
#508B TLE
'''
def main():
	import sys
	flag=False
	minim=10
	minindex=-1
	maxindex=-1
	n=sys.stdin.readline().strip()
	for i in range(len(n)):
		if (n[i]=='2' or n[i]=='4' or n[i]=='6' or n[i]=='8'or n[i]=='0') and int(n[i])<=minim:
			if minindex<0:
				minindex=i
				minim=int(n[i])
				flag=True
			else:
				maxindex=i
	if flag:	
		s=''
		for i in range(len(n)):
			if i==minindex:
				s+=n[-1]
			elif i==len(n)-1:
				s+=str(minim)
			else:
				s+=n[i]
		if maxindex>0:
			t=''
			for i in range(len(n)):
				if i==maxindex:
					t+=n[-1]
				elif i==len(n)-1:
					t+=str(minim)
				else:
					t+=n[i]
			s=str(max(int(s),int(t)))
	else:
		s='-1'
	sys.stdout.write(s)
def __starting_point():
	main()
'''
#466C
'''
def main():
	import sys
	n=int(sys.stdin.readline())
	t=tuple(map(int,sys.stdin.readline().split()))
	acc=sum(t)
	if acc % 3:
		sys.stdout.write('0')
	else:
		cnt=[]
		const=acc//3
		ss=0
		for i in t:
			if acc-ss==const:
				cnt.append(1)
			else:
				cnt.append(0)
			ss+=i 
		for i in range(n-2,-1,-1):
			cnt[i]+=cnt[i+1];		
		#print(cnt)
		ans=0
		ss=0
		for i in range(n-2):
			ss+=t[i]
			if ss==const:
				ans+=cnt[i+2]
		sys.stdout.write(str(ans)+'\n')
def __starting_point():
	main()
'''
#285B
def main():
	from sys import stdin,stdout
	import collections
	stack=collections.deque()
	n,s,t=list(map(int,stdin.readline().split()))
	M=tuple(map(int,stdin.readline().split()))
	visited=list(0 for x in range(n))
	count=0
	stack.appendleft(s-1)
	while(len(stack)):
		top=stack.popleft()
		if top==t-1:
			break
		else:
			if not visited[M[top]-1]:
				stack.appendleft(M[top]-1)
				visited[M[top]-1]=1
				count+=1
	if top==t-1:
		stdout.write(str(count)+'\n')
	else:
		stdout.write('-1\n')
def __starting_point():
	main()

__starting_point()
