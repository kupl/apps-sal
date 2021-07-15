import sys



for t in range(int(sys.stdin.readline())):


	a, b = list(map(int, sys.stdin.readline().split()))
	x, y = list(map(int, sys.stdin.readline().split()))
	a, b = min(a, b), max(a, b)
	x, y = min(x, y), max(x, y)
	if b == y and b == a + x:
		sys.stdout.write("Yes\n")
	else:
		sys.stdout.write("No\n")

