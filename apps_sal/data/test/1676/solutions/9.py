3

# def gen(n, b):
# 	import random
# 	yield '{} {}'.format(n, b)
# 	t = 0
# 	for i in range(n):
# 		t += random.randrange(1, 1e7)
# 		d = random.randrange(1, 1e7)
# 		yield '{} {}\n'.format(t, d)

# def input():
# 	g = gen(200000, 200000)

# 	return next(g)

n, b = map(int, input().split())

ends = []

for i in range(n):
    t, d = map(int, input().split())

    while len(ends) > 0 and ends[0] <= t:
        ends.pop(0)

    q = len(ends) - 1

    if q == b:
        print(-1, end=' ')
        continue

    if not ends:
        ends.append(t + d)
    else:
        ends.append(ends[-1] + d)

    print(ends[-1], end=' ')
