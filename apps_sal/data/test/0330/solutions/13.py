# vars: get_hopper, p, q, x, y
def get_hopper(x1):
	for hopper in range(2, 1+min(p, int(x1**.5))):
		if x1 % hopper == 0:
			return hopper
p, y = list(map(int, input().split()))
for x in range(y, p, -1):
	if get_hopper(x) is None:
		print(x)
#
		return
print('-1')

