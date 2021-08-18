'''
def main():
	from sys import stdin,stdout
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	import collections
	N,I =map(int,stdin.readline().split())
	visited=list(0 for x in range(N))
	G=collections.defaultdict(list)
	groups=[0]
	for _ in range(I):
		a,b=map(int,stdin.readline().split())
		G[a].append(b)
		G[b].append(a)
	q=collections.deque()
	flag=0
	for i in range(N):
		if not visited[i]:
			q.append(i)
			visited[i]=flag+1
			groups[flag]+=1
			while len(q):
				top=q.popleft()
				for j in G[top]:
					if visited[j]!=visited[top]:
						visited[j]=flag+1
						groups[flag]+=1
						q.append(j)
			flag+=1
			groups.append(0)
	counter=0
	for i in range(len(groups)-1):
		for j in range(i+1,len(groups)):
			counter+=groups[i]*groups[j]
	stdout.write(str(counter))
def __starting_point():
	main()
'''
'''
import collections
class Graph:
	def __init__(self):
		self.nodes=set()
		self.edges=collections.defaultdict(list)
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
	for _ in range(int(stdin.readline())):
		n,m=map(int,stdin.readline().split())
		G=Graph()
		for i in range(n):
			G.add_node(i+1)
		for i in range(m):
			a,b,c=map(int,stdin.readline().split())
			G.add_edge(a,b,c)
		initial=int(stdin.readline())
		v,p=dijsktra(G, initial)
		for i in range(1,n+1):
			if i!=initial:
				k=v.get(i,-1)
				stdout.write(str(k)+' ')
		stdout.write('\n')
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	string=stdin.readline().strip()
	l=len(string)
	
	arrlen=(l*(l-1))//2
	arr=list(0 for x in range(arrlen))
	f=0
	c=l-1
	for i in range(l-1):
		for j in range(i+1,l):
			if string[i]==string[j]:
				arr[f+j-i-1]=1
		f+=c
		c-=1
	if any(arr):
		
	else:
		if l & 1:
			stdout.write('First')
		else:
			stdout.write('Second')
	arr=list(list(0 for i in range(l)) for j in range(l))
	for i in range(l):
		for j in range(l):
			if string[i]==string[j]:
				arr[i][j]=1
	maxim=0
	for i in range(0,l*(l-1)-2,l+1):
		a,b=i+1,i+2
		acount=0
		x=a//5
		y=a%5
		acount=arr[x][y]		
		x-=1
		y-=1
		while x>=0 and y>=0:
			acount+=arr[x][y]
			x-=1
			y-=1
		x=b//5
		y=b%5
		bcount=arr[x][y]		
		x-=1
		y-=1
		while x>=0 and y>=0:
			bcount+=arr[x][y]
			x-=1
			y-=1
		maxim=max((acount,bcount,maxim))
	maxim=max(maxim,arr[l-2][l-1])
	maxim=(maxim<<1)^1
	delta=l-maxim
	if delta & 1:
		stdout.write('Second')
	else:
		stdout.write('First')
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	import collections
	s=stdin.readline().strip()
	count=collections.Counter(s)
	l=list(filter(lambda x: count[x] & 1,list(x for x in count)))
	removed=sum(list(count[x] for x in l))-max(list(count[x] for x in l)+[0])
	if removed & 1:
		stdout.write('Second')
	else:
		stdout.write('First')
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	n,m=map(int,stdin.readline().split())
	if m:
		dirty=sorted(map(int,stdin.readline().split()))
		if dirty[0]==1 or dirty[-1]==n:
			stdout.write('NO')
		else:
			flag=True
			for i in range(m-2):
				if dirty[i+1]==dirty[i]+1 and dirty[i+2]==dirty[i]+2:
					flag=False
					break
			if flag:
				stdout.write('YES')
			else:
				stdout.write('NO')
	else:
		stdout.write('YES')
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	n,t=map(int,stdin.readline().split())
	arr=list(map(int,stdin.readline().split()))
	maxim=0
	curr_sum=arr[0]
	i=0
	j=1
	if curr_sum <=t:
		count=1
	else:
		curr_sum=0
		count=0
		i=1
		j=2
	while j<n:
		if curr_sum+arr[j]<=t:
			count+=1
			curr_sum+=arr[j]
			j+=1
		else:
			maxim=max(count,maxim)
			if curr_sum:
				curr_sum-=arr[i]
				count-=1
			else:
				j+=1
			i+=1
	maxim=max(count,maxim)
	stdout.write(str(maxim))
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	p,q,l,r=map(int,stdin.readline().split())
	a=[]
	b=[]
	visited=list(0 for x in range(r-l+1))
	for i in range(p):
		x,y=map(int,stdin.readline().split())
		a.append(x)
		b.append(y)
	for i in range(q):
		x,y=map(int,stdin.readline().split())
		x+=l
		y+=l
		for j in range(p):
			lower=max(0,a[j]-y)
			upper=min(b[j]-x,r)+1
			if upper > lower:
				delta=upper-lower
				visited[lower:upper]=list(1 for x in range(delta))
	stdout.write(str(visited[:r-l+1].count(1)))
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	n,k=map(int,stdin.readline().split())
	a=tuple(map(int,stdin.readline().split()))
	minim=min(a)
	maxim=max(a)
	arr=list(a)	
	for i in range(n):
		arr[i]-=minim
	if max(arr) > k:
		stdout.write('NO')
	else:
		stdout.write('YES\n')
		for i in a:
			stdout.write('1 '*minim)
			for j in range(i-minim):
				stdout.write(str(j%k+1)+' ')
			stdout.write('\n')
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	n,p=[],[]
	for _ in range(int(stdin.readline())):
		last=int(stdin.readline())
		if last<0:
			n.append(-1*last)
		else:
			p.append(last)
	if sum(p)>sum(n):
		stdout.write('first')
	elif sum(n)>sum(p):
		stdout.write('second')
	else:
		maxim=max(n,p)
		if maxim==p:
			if maxim==n:
				if last<0:
					stdout.write('second')
				else:
					stdout.write('first')
			else:
				stdout.write('first')
		else:
			stdout.write('second')
		
def __starting_point():
	main()
'''


def main():
    from sys import stdin, stdout
    m, n = list(map(int, stdin.readline().split()))
    minim = min(m, n)
    stdout.write(str(minim + 1) + '\n')
    if n == minim:
        for i in range(minim + 1):
            stdout.write(str(m) + ' ' + str(i) + '\n')
            m -= 1
    else:
        for i in range(minim + 1):
            stdout.write(str(i) + ' ' + str(n) + '\n')
            n -= 1


def __starting_point():
    main()


__starting_point()
