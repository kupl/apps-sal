#The Text Splitting.py
import os
n, a, b = list(map(int, input().split()))
s = input()
maxn = n // a
# print(s)
x = -1
for i in range(0, maxn+1):
	tmp = n - a*i
	if tmp % b == 0:
		x = i
		break
if x != -1:
	print(x + (n - a*x) // b)
	out = ""
	for i in range(0, x):
		out = s[a*i:(i+1)*a]
		print(out)
	y = (n - a*x) // b
	for i in range(0, y):
		out = s[b*i+a*x:(i+1)*b+a*x]
		print(out)
else:
	print("-1")
#os.system("pause")

