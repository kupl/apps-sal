leftmost = 1000000
rightmost = leftmost-1
all_books = dict()
q = int(input())
for _ in range(q):
	q_type, q_book = input().split()
	if q_type == "L":
		leftmost -= 1
		all_books[q_book] = leftmost
	elif q_type == "R":
		rightmost += 1
		all_books[q_book] = rightmost
	else:
		print(min(rightmost-all_books[q_book], all_books[q_book]-leftmost))

