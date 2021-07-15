# vars: c1, c2, c3, ins, max_val, mid_val, min_val, n, res, res2, t1, t2, t3, x
from collections import Counter
n = int(input())
ins = input()
x = Counter(list(map(int, ins.split())))
max_val = max(x.keys())
min_val = min(x.keys())
if max_val - min_val < 2:
	print(n)
	print(ins)
else:
	mid_val = (min_val+max_val)//2
	c1, c2, c3 = x[min_val], x[mid_val], x[max_val]
	t1, t2 = c2 // 2, c2 % 2
	t3 = min(c1, c3)
	res = min((c1+t2+c3, (c1+t1, t2, c3+t1)), (c1+c2+c3-t3*2, (c1-t3, c2+t3*2, c3-t3)))
	print(res[0])
	res2 = []
	for k, v in zip((min_val, mid_val, max_val), res[1]):
		res2.extend([k]*v)
	print(*res2)
#	res = min((c1+t1, t2, c3+t1), (c1-t3, c2+t3*2, c3-t3))
#	res1 = 0
#	for vs in zip((c1, c2, c3), res):
#		res1 += min(vs)
#	print(res1)
#	res2 = []
#	for k, v in zip((min_val, mid_val, max_val), res):
#		res2.extend([k]*v)
#	print(*res2)

