def calc(n):
	return 3*((n*(n+1)))//2 - n
def binSearch(start, end, num):
	mid = (start+end)//2
	a = calc(mid)
	b = calc(mid + 1)
	if(a<=num and b>num):
		return a
	elif(a<num):
		return binSearch(mid+1, end, num)
	return binSearch(start, mid-1, num)
for tt in range(int(input())):
	n = int(input())
	c = 0
	while(n>1):
		n -= binSearch(1, n, n)
		c+=1
	print(c)
