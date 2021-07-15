N = [int(i) for i in input().split()]

n = N[0]
a = N[1]
b = N[2]

if n > a*b :
	print (-1)
else :
	dem = [int (i) for i in range (1,n+1,2)]
	resp = [int (i) for i in range (2,n+1,2)]
	i = 0
	res = []

	l_r = len(resp)
	i_r = 0

	l_d = len(dem)
	i_d = 0
	k = 0
	for i in range(a) :
		if k == 0 :
			k = 1
		else :
			k = 0
		res = []
		for j in range (b) :
			if k == 1 :
				if j % 2 == 0 :
					if i_d < l_d:
						res.append (dem[i_d])
						i_d += 1
					else :
						res.append (0)
				else :
					if i_r < l_r :
						res.append (resp[i_r])
						i_r += 1
					else :
						res.append (0)
			else :
				if j % 2 == 1 :
					if i_d < l_d:
						res.append (dem[i_d])
						i_d += 1
					else :
						res.append (0)
				else :
					if i_r < l_r :
						res.append (resp[i_r])
						i_r += 1
					else :
						res.append (0)
		print (*res)
