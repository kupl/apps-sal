__author__ = 'Lipen'

def actions(n, k, a):
	smin = -1
	answer = 1

	for i in range(k):
		s = sum(a[i::k])
		if s<smin or smin==-1:
			smin=s
			answer=i+1

	return answer

def main():
	n,k = list(map(int, input().split()))
	a = list(map(int, input().split()))

	print(actions(n, k ,a))

def __starting_point(): main()
__starting_point()
