import math
def at(n):
	return math.degrees(math.atan(n))

def main():
	a, b, x = [int(p) for p in input().split(" ")]
	V = a * a * b
	if x < V / 2:
		print((at(a * b * b / (2 * x))))
	else:
		print((at(2*(a*a*b-x)/a**3)))

main()

