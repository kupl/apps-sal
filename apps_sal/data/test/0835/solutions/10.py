b, s, c = 0, 0, 0
for i in input():
	if i == 'B':
		b += 1
	elif i == 'S':
		s += 1
	else:
		c += 1
nb, ns, nc = list(map(int,input().split()))
pb, ps, pc = list(map(int,input().split()))
money = int(input())


num = nb
if not b == 0:
    num = min(num, nb // b)
if not c == 0:
    num = min(num, nc // c)
if not s == 0:
    num = min(num, ns // s)

nb -= b * num
ns -= s * num
nc -= c * num

upper = money
lower = 0

def get_num():
    nonlocal  nb, ns, nc, pb, ps, pc, upper, lower
    mid = (upper + lower) >> 1
    while lower <= upper:
    	mid = (lower + upper) >> 1
    	need = 0
    	if mid * b > nb:
    		need += (mid * b - nb) * pb
    	if mid * s > ns:
    		need += (mid * s - ns) * ps
    	if mid * c > nc:
    		need += (mid * c - nc) * pc
    	if need == money:
    		return mid
    	elif need < money:
    		lower = mid + 1
    	else:
    		upper = mid - 1
    return upper

addition = get_num()

if addition > 0:
	print(addition + num)
else:
	print(num)




