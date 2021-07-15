import sys





[n,m] = list(map(int, sys.stdin.readline().split()))


lamps = [0 for x in range(n+1)]

buttons = list(map(int, sys.stdin.readline().split()))

for b in buttons:
	for i in range(b, n+1):
		if not lamps[i]:
			lamps[i] = b

print(" ".join(map(str, lamps[1:])))












