import math 
def __starting_point():
	n,k = list(map(int,input().split()))
	s = input()
	s = list(s)
	ls = set(s)
	flag = 1
	for i in ls:
		if s.count(i)>k:
			flag = 0
	if flag :
		print("YES")
	else:
		print("NO")


__starting_point()
