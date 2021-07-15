''' بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ '''
#codeforces1215A_live
gi = lambda : list(map(int,input().split()))
a, b, x, y, n = [gi()[0] for _ in range(5)]
l = [x for _ in range(a)]
l += [y for _ in range(b)]
l.sort()
mi = 0
nn = n
cur = 0
while nn:
	if nn < l[cur]:
		break
	nn -= l[cur]
	mi += 1
	cur += 1
nn = n
nn -= (x - 1) * a + (y - 1) * b
ma = 0
for k in range(a + b):
	if nn <= 0:
		break
	nn -= 1
	ma += 1
print(ma, mi)
