def reachable(es, source):
	ret = {source}
	Q = [source]
	while Q:
		cur = Q.pop()
		for nxt in es[cur]:
			if nxt not in ret:
				Q.append(nxt)
				ret.add(nxt)
	return ret

def BellmanFord(V:int, es:list, source=0):
	INF = float("inf")
	D = [INF]*V
	D[source] = 0
	for _ in range(V):
		upd = False
		for f, t, c in es:
			tmp = D[f] + c
			if D[t] > tmp:
				D[t] = tmp
				upd = True
		if not upd:
			return D[-1]
	else:
		return None
	
def main():
	N,M,P,*L=map(int,open(0).read().split())
	fwd = [[] for _ in range(N)]
	bwd = [[] for _ in range(N)]
	for a,b in zip(L[::3],L[1::3]):
		fwd[a-1].append(b-1)
		bwd[b-1].append(a-1)
	judge = reachable(fwd,0) & reachable(bwd,N-1)
	G = [(a-1,b-1,P-c) for a,b,c in zip(*[iter(L)]*3) if a-1 in judge and b-1 in judge]
	ans = BellmanFord(N,G)
	if ans==None:
		print(-1)
	else:
		print(max(0,-ans))

def __starting_point():
	main()
__starting_point()
