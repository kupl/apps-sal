#Bhargey Mehta (Junior)
#DA-IICT, Gandhinagar
import sys, math
MOD = 998244353
#sys.stdin = open('input.txt', 'r')

for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	z = a.count(0)
	s = sum(a)
	ans = z + (s+z == 0)
	print(ans)
