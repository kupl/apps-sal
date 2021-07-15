N, Q = list(map(int, input().split()))

area_W = N - 2
area_H = N - 2

walls_H = []
walls_V = []

count = (N - 2) * (N - 2)

# search smallest i ( s <= i < e ) such that f(i) == True
def bisearch_smallest(f, s, e = None):
	if e == None:
		e = s - 1
		s = 0
	else:
		e -= 1
	
	while s < e:
		m = (s + e) // 2
		if f(m):
			e = m
		else:
			s = m + 1
	
	if s == e and f(s):
		return s
	else:
		return -1

for _ in range(Q):
	q, i = input().split()
	i = int(i) - 2
	if q == "1":
		if i < area_W:
			area_W = i
			count -= area_H
			walls_H.append((i, area_H))
		else:
			j = bisearch_smallest(lambda j: walls_H[j][0] < i, 0, len(walls_H))
			count -= walls_H[j][1]
	else:
		if i < area_H:
			area_H = i
			count -= area_W
			walls_V.append((i, area_W))
		else:
			j = bisearch_smallest(lambda j: walls_V[j][0] < i, 0, len(walls_V))
			count -= walls_V[j][1]

#print(area_W, area_H)
print(count)

