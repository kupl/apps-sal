import sys


[n,a,b] = list(map(int, sys.stdin.readline().split()))

buttons = list(map(int, sys.stdin.readline().split()))

res = []

for x in buttons:
	money = int(1.0 * x * a / b)
	# print("money =", money)
	rest = x - 1.0 * money * b / a
	# print("rest =", rest)
	res.append(int(rest))

print(" ".join(map(str, res)))










