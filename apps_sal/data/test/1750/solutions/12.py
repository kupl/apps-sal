from collections import deque
n = int(input())
dic = {}
for i in range(n):
	dic[i]=[]
for i in range(n-1):
	a,b = map(int,input().split())
	dic[a-1].append(b-1)
	dic[b-1].append(a-1)
color = {}
prevcolor = {}
color[0] = 1
prevcolor[0] = 1
lis = deque()
lis.append(0)
visited = {}
while(len(lis)!=0):
	t = lis.popleft()
	col = 0
	visited[t] = 1
	prev = prevcolor[t]
	for i in dic[t]:
		try:
			z = visited[i]
		except:
			while(col==prev or col==color[t] or col==prevcolor[t]):
				col+=1
			color[i] = col
			prevcolor[i] = color[t]
			lis.append(i)
			prev = col

print(max(color.values())+1)
for i in range(n):
	print(color[i]+1,end=" ")
