def get_input_list():
	return list(map(int, input().split()))
def sort_(p):
	np = []
	for i in p:
		np.append([i[0],-i[1]])
	np.sort()
	return np

def distance(A,B):
	return abs(B[0] - A[0]) + abs(B[1] - A[1])

n = int(input())
p_ = []
for _ in range(n):
	p_.append(get_input_list())
d = {}
for i in p_:
	if (str(max(i))) in d:
		d[str(max(i))].append(i)
	else:
		d[str(max(i))] = [i]
l = [int(i) for i in d]
l.sort()
left = [0,0]
right = [0,0]
sleft = 0
sright = 0
for i_ in l:
	i = str(i_)
	p = sort_(d[i])
	left_ = p[0]
	right_ = p[-1]
	a1 = distance(left, left_)
	b1 = distance(left, right_)
	a2 = distance(right, left_)
	b2 = distance(right, right_)
	c = distance(p[0],p[-1])

	sl = sleft
	sr = sright

	sleft = min(sr + a1, sl + a2) + c
	sright = min(sr + b1, sl + b2) + c

	left = left_
	right = right_
print(min(sleft, sright))
