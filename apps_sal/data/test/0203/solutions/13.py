from collections import deque

n = int(input())
a = [x for x in input()]

r1, r2 = int(0), int(0)

for x in a:
	if x == 'R':
		r1 += 1
	else:
		r2 += 1

q = deque(a)

c1, c2 = int(0), int(0)

while True:
	now = q.popleft()
	if not r1 or not r2:
		print(now)
		break
	if now == 'R':
		if c2:
			c2 -= 1
			r1 -= 1
		else:
			c1 += 1
			q.append(now)
	else:
		if c1:
			c1 -= 1
			r2 -= 1
		else:
			c2 += 1
			q.append(now)

