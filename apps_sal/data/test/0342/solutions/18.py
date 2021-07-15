from sys import stdin
# stdin=open('input.txt')

def input():
	return stdin.readline().strip()


# from sys import stdout
# stdout=open('input.txt',mode='w+')

# def print1(x, end='\n'):
# 	stdout.write(str(x) +end)


# a, b = map(int, input().split())

# l = list(map(int, input().split()))


# CODE BEGINS HERE.................

a, b, c = list(map(int, input().split()))

print(2 * c + 2 * min(a, b) + (a - min(a, b) > 0 or b - min(a, b) > 0))


# CODE ENDS HERE....................
# stdout.close()


