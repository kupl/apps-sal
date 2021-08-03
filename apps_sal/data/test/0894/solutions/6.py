from math import floor
s = input()
sl = s.split(' ')
x = int(sl[0])
y = int(sl[1])
dis = abs(x) + abs(y)
# if type(dis) is 'int':
if x > 0:
    if y > 0:
        print('0 {} {} 0'.format(dis, dis))
    else:
        print('0 {} {} 0'.format(-dis, dis))
else:
    if y > 0:
        print('{} 0 0 {}'.format(-dis, dis))
    else:
        print('{} 0 0 {}'.format(-dis, -dis))
# else:
# 	if x > 0:
# 		if y > 0:
# 			print('0 {} {} 0'.format(floor(dis)+1, floor(dis)+1))
# 		else:
# 			print('0 {} {} 0'.format(floor(dis)+1, -(floor(dis)+1)))
# 	else:
# 		if y > 0:
# 			print('0 {} {} 0'.format(-(floor(dis)+1), floor(dis)+1))
# 		else:
# 			print('0 {} {} 0'.format(-(floor(dis)+1), -(floor(dis)+1)))
