import sys
while True:
	try:
		W, L = [int(i) for i in input().split()]
		river = [int(i) for i in input().split()]

		sum_seq = sum(river[:L])
		frogs = sum_seq

		for i in range(L,W-1):
			sum_seq = sum_seq + river[i] - river[i-L]
			frogs = min(sum_seq, frogs)
		print(frogs)
	except EOFError:
		return
