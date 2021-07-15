hh, mm = list(map(int, input().split()))

h, d, c, n = list(map(int, input().split()))

if hh >= 20:
	c *= 0.8
	cost1 = cost2 = (h + n - 1) // n * c
else:
	cost1 = (h + n - 1) // n * c
	h += (20 * 60 - hh * 60 - mm) * d
	c *= 0.8
	cost2 = (h + n - 1) // n * c

print('{:.10f}'.format(min(cost1, cost2)))

