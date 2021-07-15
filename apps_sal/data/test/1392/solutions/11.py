__author__ = 'Lipen'

def actions(n,k,a):
	answer = 0
	r = list(range(k+1))

	for i in a:
		if all(x in list(set(i)) for x in r):
			answer+=1

	return answer

def main():
	n, k = list(map(int, input().split()))
	a = []
	for i in range(n):
		a.append(list(map(int, input())))

	print(actions(n,k,a))

def __starting_point(): main()
__starting_point()
