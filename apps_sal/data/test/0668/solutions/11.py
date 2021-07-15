n = int(input())
students = list(map(int, input().split(' ')))
indexes = list(zip(range(n),students))[1:]
indexes.sort(key = lambda x: x[1], reverse = True)
indexes = [(0,students[0])]+indexes
#print(indexes)
last_informed_index = 0
out = []
last_used = 0
while last_informed_index<n and last_used!=n:
	if last_used<=last_informed_index:
		for i in range(last_informed_index+1, min(last_informed_index+indexes[last_used][1]+1, n)):
			out.append("%d %d"%(indexes[last_used][0]+1, indexes[i][0]+1))
		last_informed_index=min(last_informed_index+indexes[last_used][1], n-1)
		last_used+=1
	else:
		print(-1)
		return
print(len(out))
print('\n'.join(out))
