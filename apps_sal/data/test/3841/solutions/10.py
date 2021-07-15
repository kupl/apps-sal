import sys

inp = input().split()
p = int(inp[0])
k = int(inp[1])
r = 0
pow = 1
while 1:
	if r % 2 == 0 and pow >= p:
		break
	r = r + 1
	pow = pow * k
i = r
ans = ""
while i >= 0:
	j = 0
	s = 0
	x = pow // k
	while x > 0:
		s = s + (k - 1) * x
		x = (x // k) // k
	if i == 0:
		j = p
	elif i % 2 == 0:
		while p - pow * j > 0 and p - pow * (j + 1) >= -s:
			j = j + 1
		p = p - pow * j
	else:
		while p + pow * j < 0 and  p + pow * (j + 1) <= s:
			j = j + 1
		p = p + pow * j
	
	if j != 0 or ans != "":
		ans = str(j) + " " + ans
	else:
		r = r - 1
#	print(p)
	i = i - 1
	pow = pow // k
print(r + 1)
print(ans)
