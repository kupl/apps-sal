
n = int(input())
a = {'purple':'Power', 'green' : 'Time', 'blue' : 'Space', 'orange' : 'Soul', 'red' : 'Reality', 'yellow' : 'Mind'}
for _ in range(n):
	s = input()
	a[s] = 1
print (6-n)
for i in a:
	if a[i]!=1:
		print (a[i])
