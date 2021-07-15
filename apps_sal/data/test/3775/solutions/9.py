#!/usr/bin/env python3

[n, m] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))
bis = list(map(int, input().strip().split()))

ais = [set(ais[2*i: 2*i + 2]) for i in range(n)]
bis = [set(bis[2*i: 2*i + 2]) for i in range(m)]

def check(pair, pairs):
	res = []
	for p in pairs:
		s = pair & p
		if len(s) == 1:
			res.append(s.pop())
	res = list(set(res))
	if len(res) == 1:
		return res[0]
	elif len(res) > 1:
		return -1
	else:
		return 0


va = [check(a, bis) for a in ais]
vb = [check(b, ais) for b in bis]

vap = [v for v in va if v > 0]
vbp = [v for v in vb if v > 0]

vap = set(vap)
vbp = set(vbp)

vabp = vap & vbp

if -1 in va or -1 in vb:
	print(-1)
elif len(vabp) > 1:
	print(0)
else:
	print(vabp.pop())




# Made By Mostafa_Khaled

