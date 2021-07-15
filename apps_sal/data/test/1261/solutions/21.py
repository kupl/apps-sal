from math import ceil
n = int(input())
if n == 1:
    print(1)
    return
if n == 2:
	print('1 2')
	return
elif n == 3:
	print('1 1 3')
	return
o = 0
if n&1: 
	n -= 1
	o = 1
ans, i, t = '1 ' * ceil(n / 2), 1, n
n = ceil(n/2)
j = 2
while n > 1:
	ans += (str(j) + ' ') * ((n // 2) if t&1 else ceil(n/2))
	i += 1
	j = pow(2, i)
	n //= 2
print(('1 ' if o else '') + ans + str((j//2)*(t//(j//2)))) 
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 4 4 4 4 8 8
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 4 4 4 4 8 8 16
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 4 4 4 4 8 8 24

