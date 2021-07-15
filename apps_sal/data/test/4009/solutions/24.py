# stdin=open('input.txt')
from sys import stdin

def input():
	return stdin.readline()[:-1]


# # stdout=open('output.txt',mode='w+')

# # def print(x, end='\n'):
# # 	stdout.write(str(x) +end)


# # a, b = map(int, input().split())

# # l = list(map(int, input().split()))







# CODE BEGINS HERE.................


n, x, y = list(map(int, input().split()))
s = input()
ones = s[-1*x:].count('1') - (s[-1 * y - 1] == '1') + (s[-1 * y - 1] == '0')

print(ones)


#CODE ENDS HERE....................

#stdout.close()


