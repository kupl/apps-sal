def main():
	n = int(input())
	x = [int(v) for v in input().split()]
	x.sort()
	closest = x[0]
	farest = x[-1]
	startPoint = 0
	sofar = float('inf')
	for i in range(0, farest+1):
		p = i
		cur = 0
		for j in range(len(x)):
			cur += (x[j] - p)**2
		if cur < sofar:
			sofar = cur
	return sofar





def __starting_point():
    print((main()))

__starting_point()
