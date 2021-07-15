h,m,s,t1,t2 = list(map(int,input().split()))
h %= 12
arr = []
arr.append(h*30 + m/2 + s/120)
arr.append(6*m + s/10)
arr.append(6*s)
arr.sort()
arr = arr + [(360 + arr[0])]

t1 *= 30
t2 *= 30

x1 = -1
x2 = -1
for i in range(3):
	if((arr[i] <= t1 and t1 <= arr[i+1]) or (arr[i] <= t1+360 and t1+360 <= arr[i+1])):
		x1 = i
	if((arr[i] <= t2 and t2 <= arr[i+1]) or (arr[i] <= t2+360 and t2+360 <= arr[i+1])):
		x2 = i

print('YES' if x1==x2 else 'NO')

