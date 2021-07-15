n,m=map(int,input().split())
cols=['']*m
count=0
for i in range(n):
	line=input().split()
	if ('0' in line) and ('1' in line):
		count+=line.count('0')
		start=line.index('1')+1
		end=m-line[::-1].index('1')-1
		count+=line[start:end].count('0')
	for j in range(m):
		cols[j]+=line[j]

for i in range(m):
	cur=cols[i]
	if ('0' in cur) and ('1' in cur):
		count+=cur.count('0')
		start=cur.index('1')+1
		end=n-cur[::-1].index('1')-1
		count+=cur[start:end].count('0')
print(count)
