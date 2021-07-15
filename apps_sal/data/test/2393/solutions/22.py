import math
t = int(input())
for j in range(t):
	a = list(input())
	res = ''
	k = 0
	i =0
	while i < len(a)-2:
		if a[i] == 'o':
			if a[i+1] == 'n':
				if a[i+2] == 'e':
					if i+3 < len(a) and a[i+3] != 'e':
						res += str(i+3)+' '
						k += 1
					else:
						res += str(i+2)+' '
						k += 1
					i += 2
		if a[i] == 't':
			if a[i+1] == 'w':
				if a[i+2] == 'o':
					if i+3 < len(a) and a[i+3] != 'o':
						res += str(i+3)+' '
						k += 1
					else:
						res += str(i+2)+' '
						k += 1
					i += 2
		i += 1
	print(k)
	print(res)
