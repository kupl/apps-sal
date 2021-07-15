n = int(input())
A = []
for i in range(n):
	b, a = map(int, input().split())
	A.append(a)
	if b != a:
		print("rated")
		break
else:
	B = sorted(A)
	A.reverse()
	if A == B:
		print("maybe")
	else:
		print("unrated")
