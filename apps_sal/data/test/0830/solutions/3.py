f = input()
s = input()
a = f.split(' ')
n = int(a[0])
k = int(a[1])
a = s.split(' ')

i = 0
while(i < n):
	a[i] = int(a[i])
	i = i + 1

ans = -1
v1 = list()
v2 = list()
while(k > 0):
	posmn = -1
	posmx = -1
	mn = 2**16
	mx = -1
	i = 0
	while(i < n):
		if(mn > a[i]):
			mn = a[i]
			posmn = i
		if(mx < a[i]):
			mx = a[i]
			posmx = i
		i = i + 1
	if(mx == mn):
		ans = 0
		break
	v1.append(posmx + 1)
	v2.append(posmn + 1)
	a[posmx] = a[posmx] - 1
	a[posmn] = a[posmn] + 1
	k = k - 1
i = 0
mx = -1
mn = 2**16
while(i < n):
	mn = min(mn, a[i])
	mx = max(mx, a[i])
	i = i + 1
ans = mx - mn
print(str(ans) + ' ' + str(len(v1)))
i = 0
while(i < len(v1)):
	print(str(v1[i]) + ' ' + str(v2[i]))
	i = i + 1
