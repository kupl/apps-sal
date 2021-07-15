n, p = list(map(int,input().split()))
l = list(map(int,input().split()))
trees_p = set(l)
trees_l = set(l)
zaj = {}
for i in l:
	zaj[i] = 1
	
dupa = 0
odp = []
odl = 0
import sys
while True:
	odl += 1
	to_rem = []
	for t in trees_l:
		try:
			zaj[t-odl]
			to_rem.append(t)
		except Exception:
			zaj[t-odl] = 1
			odp.append(t-odl)
			dupa += odl
			if len(odp) == p:
				print(dupa)
				print(*odp)
				return
	for x in to_rem:
		trees_l.remove(x)
	
	to_rem = []
	for t in trees_p:
		try:
			zaj[t+odl]
			to_rem.append(t)
		except Exception:
			zaj[t+odl] = 1
			odp.append(t+odl)
			dupa += odl
			if len(odp) == p:
				print(dupa)
				print(*odp)
				return
	for x in to_rem:
		trees_p.remove(x)
			
	


