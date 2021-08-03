N, cnt = [int(1e5 + 5000), int(0)]


class edg:
    pnt, nxt = [int(0), int(0)]


fir = [0] * N
ed = [edg()]
for i in range(1, N):
    ed.append(edg())


def link(u, v):
    nonlocal cnt
    cnt += 1
    ed[cnt].nxt = fir[u]
    fir[u] = cnt
    ed[cnt].pnt = v


#	print(ed[1].pnt,ed[2].pnt,ed[3].pnt)
#	print(cnt,ed[1].pnt,ed[1].nxt)
#	print(ed[2].pnt)
# print(ed[0].pnt)
n, k = list(map(int, input().split(" ")))
#print(n," ",k)
q = [0] + list(map(int, input().split(" ")))
# print(q[1])
# link(1,1)
# '''
for i in range(1, k + 1):
    #	u,v=[1,1]
    u, v = [q[i], i]
    link(u, v)
#	print(u,v)
# '''
# stay
'''
print(q)
u=5
e=fir[u]
print(ed[2].pnt)
'''
'''
print(ed[2].pnt,ed[3].pnt)
ed[2].pnt=1
print(ed[2].pnt,ed[3].pnt)
'''
ans = int(0)
for i in range(1, n + 1):
    if(fir[i] == 0):
        ans += 1
# left
for i in range(2, n + 1):
    minx, maxx = [(1 << 27), -(1 << 27)]
    u = i
    e = fir[u]
    while(e != 0):
        minx = min(minx, ed[e].pnt)
        e = ed[e].nxt
    u = i - 1
    e = fir[u]
    while(e != 0):
        maxx = max(maxx, ed[e].pnt)
        e = ed[e].nxt
    if(minx > maxx):
        ans += 1
#		print(i,i-1)
# right
for i in range(1, n):
    minx, maxx = [(1 << 27), -(1 << 27)]
    u = i
    e = fir[u]
    while(e != 0):
        minx = min(minx, ed[e].pnt)
        e = ed[e].nxt
    u = i + 1
    e = fir[u]
    while(e != 0):
        maxx = max(maxx, ed[e].pnt)
        e = ed[e].nxt
    if(minx > maxx):
        ans += 1
#		print(i,i+1)
'''
	if(i==4):
#		print(minx,maxx)
		u=i+1
		e=fir[u]
		while(e!=0):
			print(ed[e].pnt)
			e=ed[e].nxt
'''
print(ans)
