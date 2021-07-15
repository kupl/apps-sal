def lowbit(x):
	return x & (-x)
	
def solve():
	nonlocal sum, limit, list
	while(limit > 0 and sum!=0):
		if(sum-lowbit(limit)>=0):
			sum-=lowbit(limit)
			list.add(limit)
		limit-=1
	if(sum==0):
		return True
	return False
	
sum, limit = tuple(int(i) for i in input().split())
list = set()

if(solve()):
	s = str(len(list)) + "\n"
	for i in list:
		s += str(i) + " "
	print (s[:len(s)-1])
else:
	print (-1)
