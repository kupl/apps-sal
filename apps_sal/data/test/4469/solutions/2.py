q = int(input())

if q > 0:
	left = 0
	right = 0

	d = dict()

	[q_type, q_id] = input().split()
	d[q_id] = 0

	for i in range(q-1):
		[q_type, q_id] = input().split()
		if q_type == 'L':
			left -=1
			d[q_id] = left
		elif q_type == 'R':
			right += 1
			d[q_id] = right
		elif q_type == '?':
			p = d[q_id]
			print(min(p-left, right-p))
