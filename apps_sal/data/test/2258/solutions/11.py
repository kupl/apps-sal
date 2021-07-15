n,a,inv = int(input()),list(map(int,input().split())),[]
for i in range(1,n):
	for j in range(i):
		if a[i] < a[j]:inv.append((i,-a[j],-j))
inv.sort(reverse=True);r = list(range(len(inv)))
if r is not None:
	print(len(r))
	for z in r:v, _, u = inv[z];u = -u;print(u+1,v+1)
else:print("wut")
