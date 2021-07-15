__author__ = 'Lipen'


def main():
	n = int(input())
	a = list(map(int, input().split()))
	now = 0
	answer = 0

	for x in a:
		if x == -1:
			if now>0:
				now-=1
			else:
				answer+=1
		else:
			now+=x

	print(answer)

main()
