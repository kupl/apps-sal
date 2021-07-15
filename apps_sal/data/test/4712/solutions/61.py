H,W = map(int, input().split())
H += 2
W += 2
for i in range(H):
	if i == 0 or i == H-1:
		out = '#'*W
	else:
		a = input()
		out = '#{}#'.format(a)
	print(out)
