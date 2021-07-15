n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
s=list(set(a))
for i in s:
	if a.count(i)>k:
		print("NO")
		quit()
done=[]

for i in range(k):
	done.append([])
print("YES")
for i in range(k):
	print(i+1,end=' ')
	done[i].append(a[i])
for i in range(k,n):
	for j in range(k):
		if a[i] not in done[j]:
			print(j+1,end=' ')
			done[j].append(a[i])
			break
