'''input
5
5009
7
9876
10000
10
'''
def solve():
	s = input()
	ln = len(s)
	ans = []
	for i in s:
		num = int(i+(ln-1)*'0')
		if num!=0:
			ans.append(num)
		ln-=1
	print(len(ans))
	for i in ans:
		print(i,end=" ")
	print()
	return 
t = 1
t = int(input())
while t>0:
	t-=1
	solve()
