from math import gcd 
n = int(input())

fracs = []
for a in range(1, n):
	b = n - a
	if gcd(a, b) == 1 and a < b:
		fracs.append([a, b])

max_a = None
max_b = None
max_frac = -1

for frac in fracs:
	value = frac[0]/frac[1] 
	if value > max_frac:
		max_frac = value
		max_a = frac[0]
		max_b = frac[1]

print(max_a, max_b) 

