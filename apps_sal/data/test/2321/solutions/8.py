# stdin=open('input.txt')

# def input():
# 	return stdin.readline()[:-1]

# a, b = map(int, input().split())

# l = list(map(int, input().split()))


# CODE BEGINS HERE.................

for t in range(int(input())):
	n = int(input())
	a = input()

	count1 = 0
	count2 = 0
	for i in a:
		if i == '<':
			count1 += 1
		else:
			break

	a = a[::-1]

	for i in a:
		if i == '>':
			count2 += 1
		else:
			break

	print(min(count1, count2))

#CODE ENDS HERE....................



