import itertools

n = int(input())

s = input()
x = []

for k, g in itertools.groupby(s):
	l = len(list(g))
	x += [l]

bad = 0
for f, g in zip(x, x[1:]):
	bad += f + g - 1

good = n * (n+1)//2-n-bad

print(good)

