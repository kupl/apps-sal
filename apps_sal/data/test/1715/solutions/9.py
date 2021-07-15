A, B, Q = map(int, input().split())

Jinja = []
Tera = []
Ichi = []
for i in range (0, A):
	Jinja.append(int(input()))
for i in range (0, B):
	Tera.append(int(input()))
for i in range (0, Q):
	Ichi.append(int(input()))

import math
import bisect as bi

for i in range (0, Q):
	temp = Ichi[i]
	J = math.inf
	T = math.inf
	JL = bi.bisect_left(Jinja, temp)
	JR = bi.bisect_right(Jinja, temp)
	TL = bi.bisect_left(Tera, temp)
	TR = bi.bisect_right(Tera, temp)
	if JL != JR:
		J = 0
	if TL != TR:
		T = 0
	if JR == 0:
		JW = math.inf
		JE = abs(temp-Jinja[0])
	elif JL == A:
		JW = abs(temp-Jinja[A-1])
		JE = math.inf
	else:
		JW = abs(temp-Jinja[JL-1])
		JE = abs(temp-Jinja[JL])
	if TR == 0:
		TW = math.inf
		TE = abs(temp-Tera[0])	
	elif TL == B:
		TW = abs(temp-Tera[B-1])
		TE = math.inf	
	else:
		TW = abs(temp-Tera[TL-1])
		TE = abs(temp-Tera[TL])
	print(min(J+T, J+TW, J+TE, T+JW, T+JE, max(JW, TW), max(JE, TE), 2*JW+TE, 2*TE+JW, 2*JE+TW, 2*TW+JE))
