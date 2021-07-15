#input
n=int(input())
namelist=[]
for i in range(n):
	namelist.append([str(x) for x in input().split()])
plist=[int(x) for x in input().split()]



#variables
limit=min(namelist[plist[0]-1])



#main
for i in range(n-1):
	if limit<min(namelist[plist[i+1]-1]):
		limit=min(namelist[plist[i+1]-1])
	elif limit<max(namelist[plist[i+1]-1]):
		limit=max(namelist[plist[i+1]-1])
	else:
		print('NO')
		quit()

print('YES')
