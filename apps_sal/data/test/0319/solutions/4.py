import re
import math
import decimal
import bisect

def read():
	return input().strip()

n, m = [int(x) for x in read().split()]
switches = []
for i in range(n):
	switches.append(int(read(), 2))

allon = int("1"*m, 2)
for i in range(n):
	ans = 0
	for j in range(n):
		if j != i:
			ans |= switches[j]
		if ans == allon:
			print("YES")
			return
print("NO")

