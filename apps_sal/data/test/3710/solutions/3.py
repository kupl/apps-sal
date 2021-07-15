from math import gcd


def lcm(a, b):
	return (a * b) // gcd(a, b)


def main():
	n, k = list(map(int, input().split()))
	ans = 1
	a = list(map(int, input().split()))
	for i in range(n):
		tc = a[i]
		gc = gcd(tc, k)
		ans = lcm(ans, gc)
	if ans == k:
		print('Yes')
	else:
		print('No')
main()

