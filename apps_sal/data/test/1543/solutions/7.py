rides = int(input())
franxx = []
Zero = []
Two = []

for i in range(rides):
	darling = input().split()
	if (darling[1] == 'B'):
		darling[1] = 1
	elif (darling[1] == 'R'):
		darling[1] = 2
	else:
		darling[1] = 3
	franxx.append((int(darling[0]), int(darling[1])))

love = 0

hiro = ["I love Zero Two", "I love Darling"]

for zero, two in franxx:
	if (two == 3 or two == 1):
		if (hiro[0] == 'I love Zero Two'):
			Zero.append(0)
			hiro[0] = zero
		else:
			Zero.append(zero - hiro[0])
			love += zero - hiro[0]
			hiro[0] = zero
			
	if (two == 3 or two == 2):
		if (hiro[1] == 'I love Darling'):
			Two.append(0)
			hiro[1] = zero
		else:
			Two.append(zero - hiro[1])
			love += zero - hiro[1]
			hiro[1] = zero
	
	if (two == 1):
		Two.append(0)
	elif (two == 2):
		Zero.append(0)

hiro = [-1, 0]
for ride in range(rides):
	if (franxx[ride][1] == 3):
		if (hiro[0] == -1):
			hiro[0] = ride
			hiro[1] = 0
		else:
			strelizia = [0, 0]
			if ((hiro[1] & 1) == 0):
				strelizia[0] = franxx[ride][0] - franxx[hiro[0]][0]
			if ((hiro[1] & 2) == 0):
				strelizia[1] = franxx[ride][0] - franxx[hiro[0]][0]

			for darling in range(hiro[0], ride):
				if (hiro[1] & 1):
					strelizia[0] = max(strelizia[0], Zero[darling + 1])
				if (hiro[1] & 2):
					strelizia[1] = max(strelizia[1], Two[darling + 1])
			if (strelizia[0] + strelizia[1] - franxx[ride][0] + franxx[hiro[0]][0] > 0):
				love -= strelizia[0] + strelizia[1] - franxx[ride][0] + franxx[hiro[0]][0]
			hiro[0] = ride
			hiro[1] = 0
	else:
		hiro[1] |= franxx[ride][1]

print(love)
