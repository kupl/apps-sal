en = list(map(int, input().split()))
n = en[0]
k = en[1]

houses = list(map(int, input().split()))

segments = []
counter = 1
for i in range(1, n):
	if(houses[i] != houses[i-1]):
		counter+=1
	else:
		segments.append(counter)
		counter=1

segments.append(counter)
print(max(segments))
