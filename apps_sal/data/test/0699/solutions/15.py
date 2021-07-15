y, k, n = map(int, input().split())
temp = int(y / k)
temp += 1
temp = temp * k
#print (temp)
if temp > n:
	print (-1)
	return
while temp <= n:
	print (temp - y, end = ' ')
	temp += k
print ()

