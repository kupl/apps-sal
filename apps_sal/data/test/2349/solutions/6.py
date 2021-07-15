def kek(n):
	l = [0]
	l2 = []
	i = 1
	while i * i < n:
		l.append(i)
		if n // i != i:
			l2.append(n // i)
		i += 1
	if i * i == n:
		l.append(i)
	l2.reverse()
	l += l2
	return l

def main():
	for _ in range(int(input())):
		n = int(input())
		l = kek(n)
		print(len(l))
		for i in l:
			print(i, end=' ')
		print()
main()
