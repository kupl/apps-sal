ht = input()
at = input()
N = int(input())
hc = [0]*100
ac = [0]*100
for n in range(N):
	ar = input().split()
	t = int(ar[0])
	m = int(ar[2])
	if ar[1] == 'h':
		if ar[3] == 'r':
			if hc[m] < 2:
				print(ht, m, t)
				hc[m] = 2
		else:
			hc[m] += 1
			if hc[m] == 2:
				print(ht, m, t)
	if ar[1] == 'a':
		if ar[3] == 'r':
			if ac[m] < 2:
				print(at, m, t)
				ac[m] = 2
		else:
			ac[m] += 1
			if ac[m] == 2:
				print(at, m, t)

