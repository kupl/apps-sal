n,k,c=list(map(int,input().split()))
s=input()

i=0
counter=0
fslist=[]

while counter < k:
	if s[i] == "o":
		fslist.append(i)
		i += c+1
		counter += 1
	else:
		i += 1

i=-1
counter=0
felist=[]

while counter < k:
	if s[i] == "o":
		felist.append(i+n)
		i -= c+1
		counter += 1
	else:
		i -= 1

felist.reverse()

for i in range(k):
	if fslist[i] == felist[i]:
		print((fslist[i]+1))


