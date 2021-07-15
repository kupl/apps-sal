__author__ = 'Lipen'


def main():
	n,t,c = map(int, input().split())
	v = list(map(int, input().split()))
	k = 0
	answer = 0

	for i in range(n):
		x = v[i]
		if x > t:
			answer += max(0, k-c+1)
			k = 0
		else:
			k+=1
	answer += max(0, k-c+1)

	print(answer)

main()
