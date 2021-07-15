n = int(input())

a = []
b = []

for i in range(n):
	x,y = map(int,input().split())
	if x >= 0:
		a.append((x,y))
	else:
		b.append((x,y))

a.sort(key=lambda tup:tup[0])
b.sort(key=lambda tup:tup[0])
b = b[::-1]

minLength = min(len(a),len(b))

total = 0

for i in range(minLength):
	total += b[i][1] + a[i][1]

if(len(a) > minLength):
	total += a[minLength][1]
elif(len(b) > minLength):
	total += b[minLength][1]

print(total)
