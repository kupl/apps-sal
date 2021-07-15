n, xbase = list(map(int, input().split()))
xs = list(map(int, input().split()))

m, ybase = list(map(int, input().split()))
ys = list(map(int, input().split()))

x = 0
xt = 1
for c in xs[::-1]:
	x += c * xt
	xt *= xbase

y = 0
yt = 1
for c in ys[::-1]:
	y += c * yt
	yt *= ybase

if x < y:
	print('<')
elif x > y:
	print('>')
else:
	print('=')

