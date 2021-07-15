import math
def na():
	n = int(input())
	b = [int(x) for x in input().split()]
	return n,b


def nab():
	n = int(input())
	b = [int(x) for x in input().split()]
	c = [int(x) for x in input().split()]
	return n,b,c


def dv():
	n, m = list(map(int, input().split()))
	return n,m


def dva():
	n, m = list(map(int, input().split()))
	b = [int(x) for x in input().split()]
	return n,m,b


def nm():
	n = int(input())
	b = [int(x) for x in input().split()]
	m = int(input())
	c = [int(x) for x in input().split()]
	return n,b,m,c


def dvs():
	n = int(input())
	m = int(input())
	return n, m


n = int(input())
s =  input()
new =  ''
a =  0 
b =  0
for i in range(n - 1):
	s1 =  s[i]
	s2 =  s[i +  1]
	if s1 > s2:
		new  =  s1 +  s2  
		a =  i
		b  =   i +  1 
		print('YES')
		print(a +1, b +  1 )
		return
print('NO')

