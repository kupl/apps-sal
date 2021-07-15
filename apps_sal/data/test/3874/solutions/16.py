n,m=map(int,input().split())
name=[None]*n
for i in range(n):
	name[i]=input()
delete=list(map(int,input().split()))

len_pattern=len(name[delete[0]-1])
for i in range(m):
	if len(name[delete[i]-1])!=len_pattern:
		print("No")
		return

pattern=""
for i in range(len_pattern):
	cur_char=name[delete[0]-1][i]
	for j in range(m):
		if name[delete[j]-1][i]!=cur_char:
			pattern+="?"
			break;
	else:
		pattern+=cur_char

remain=[None]*(n-m)
count=0;
for i in range(n):
	if i+1 not in delete:
		remain[count]=i+1
		count+=1

for i in range(count):
	len_remain_name=len(name[remain[i]-1])
	if len_remain_name==len_pattern:
		for j in range(len_remain_name):
			cur_char=name[remain[i]-1][j]
			if pattern[j]!='?':
				if cur_char!=pattern[j]:
					break;
		else:
			print("No")
			return
else:
	print("Yes")
	print(pattern)
