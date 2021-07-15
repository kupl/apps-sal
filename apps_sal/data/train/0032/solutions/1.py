from sys import stdin
input = stdin.readline

def max_pos_coins(n):
	a = 0
	while n != 0:
		if n == 4:
			a += 3
			n = 0
			continue
		if n % 4 == 0:
			n -= 2
			a += 1
		else:
			a += n // 2
			n = n // 2 - 1
	return a

for _ in range(int(input())):
	n = int(input())
	print(max_pos_coins(n) if n % 2 == 0 else n - max_pos_coins(n - 1))

