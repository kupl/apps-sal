import collections as col

A = str(input())
B = str(input())
C = str(input())

A_queue = col.deque()
B_queue = col.deque()
C_queue = col.deque()

for i in range (0, len(A)):
	A_queue.append(A[i])
for i in range (0, len(B)):
	B_queue.append(B[i])
for i in range (0, len(C)):
	C_queue.append(C[i])

D = ['a','b','c']
  
start = 0  
for i in range (0, 300):
	if start == 0:
		if len(A_queue) == 0:
			print('A')
			return
		else:
			V = A_queue.popleft()
			start = D.index(V)
	elif start == 1:
		if len(B_queue) == 0:
			print('B')
			return
		else:
			V = B_queue.popleft()
			start = D.index(V)     
	else:
		if len(C_queue) == 0:
			print('C')
			return
		else:
			V = C_queue.popleft()
			start = D.index(V) 
