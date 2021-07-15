import sys

def input():
	return sys.stdin.readline().rstrip()

def input_split():
	return [int(i) for i in input().split()]

testCases = int(input())
answers = []
for _ in range(testCases):
	#take input
	n = int(input())
	arr = input_split()

	s = sum(arr)

	if s <= n//2:
		ans = [0]*(n//2)
	else:
		#num of ones is greater than equal to n//2
		if n%4 == 0:
			ans = [1]*(n//2)
		else:
			ans = [1]*((n//2) + 1)
		# ans = [1]*()

	answers.append(ans)
for ans in answers:
	print(len(ans))
	print(*ans, sep = ' ')

