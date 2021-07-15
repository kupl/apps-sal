'''input
284254589153928171911281811000
1009 1000
'''
from sys import stdin
import math


def check_leading_zero(nstring, index):
	if nstring[index] == '0':
		return False
	return True


def cal_first(nstring, a):
	dp1 = [-1] * len(nstring)
	remain = 0;
	for i in range(len(nstring)):
		dp1[i] = (remain * 10 + int(nstring[i])) % a		
		remain = dp1[i]
	return dp1


def cal_second(nstring, b):
	dp2 = [-1] * len(nstring)
	dp2[-1] = int(nstring[-1]) % b 
	mul = 10
	for i in range(len(nstring) - 2, -1, - 1):
		dp2[i] = ((int(nstring[i]) * mul )+ dp2[i + 1]) % b
		mul = (mul * 10) % b
	return dp2


# main starts
nstring = stdin.readline().strip()
a, b = list(map(int, stdin.readline().split()))
if len(nstring) == 1:
	print("NO")
	return

dp1 = cal_first(nstring, a)
dp2 = cal_second(nstring, b)
#print(dp1, dp2)
for i in range(len(dp1) - 1):
	if dp1[i] == 0 and dp2[i + 1] == 0:
		if check_leading_zero(nstring, i + 1):
			print('YES')
			print(nstring[:i + 1])
			print(nstring[i + 1:])
			return
else:
	print('NO')

