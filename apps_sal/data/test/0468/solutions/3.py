from math import log10
x,y = map(int, input().split())
if abs(y * log10(x) - x * log10(y)) <= 0.001:
	print('=')
elif y * log10(x) < x * log10(y):
	print('<')
else:
	print('>')
