n = int(input())
a = 1
b = 1
t = 2
while a+b <= n:
	c = b
	b = a+b
	a = c
	t = t+1
l = t*[1]
for i in range(2,t):
	l[i] = l[i-1]+l[i-2]
k = ''
for i in range(n):
	if i+1 in l:
		k = k+'O'
	else:
		k = k+'o'
print(k)

