from collections import deque
while True:
	try:
		n, max_queue_lenth = map(int, input().split())
	except EOFError:
		break

	queue = deque()
	responses = []
	for i in range(n):
		time, duration = tuple(map(int, input().split()))
		while queue and queue[0]<=time:
			queue.popleft()
		if not queue:
			queue.append(time+duration)
			responses.append(time+duration)
			continue
		else:
			if len(queue)<=max_queue_lenth:
				queue.append(queue[-1]+duration)
				responses.append(queue[-1])
			else:
				responses.append(-1)
	print(" ".join(map(str, responses)))
