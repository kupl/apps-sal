from queue import Queue as Q

def fill(start, used, a):
	q = Q()
	q.put(start)
	n = len(a)
	used[start] = start + 1
	while not q.empty():
		next = q.get()
		for i in range(n):
			if a[next][i] == '0' or used[i]:
				continue
			used[i] = start + 1
			q.put(i)

n = int(input())
p = [int(x) for x in input().split()]
a = []
for i in range(n):
	a.append(input())
used = [0] * n
lists = [[] for i in range(n)]
for i in range(n):
	if not used[i]:
		fill(i, used, a)
	lists[used[i] - 1].append(p[i])
for l in lists:
	l.sort()
for i in range(n):
	p[i] = lists[used[i] - 1][0]
	lists[used[i] - 1].pop(0)
print(' '.join(str(x) for x in p))

