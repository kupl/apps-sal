'''def bSearch(a,x,n):
	low = 0
	high = n-1
	flag = False
	while(low <= high and flag == False):
		mid = (low+high)//2
		if(a[mid] == x):
			flag = True
		else:
			if(x < a[mid]):
				high = mid - 1
			else:
				low = mid + 1
	return flag

n,k = map(int,input().split())

a = list(map(int,input().split()))

s = []
m = 0
a = sorted(a)

for i in a:
	if(i % k != 0):
		s.append(i)
		m += 1
	elif(bSearch(s,i/k,m) == False):
		s.append(i)
		m += 1

print(m)

n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
a = sorted(a)
s = []
d = {}
m = 0

for i in a:
    if(i % k != 0):
        s.append(i)
        m += 1
        d[i] = 1
    elif((i // k) not in d):
        s.append(i)
        d[i] = 1
        m += 1

print(m)
