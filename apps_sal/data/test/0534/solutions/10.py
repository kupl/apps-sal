n,k=[ int(x) for x in input().split(' ') ]
current=input()

def turn(str):
	temp=list(str)	
	for i in range(1,len(str)) :
		if str[i] == 'G' and str[i-1] == 'B' :
			temp[i-1]='G'
			temp[i]='B'
	ret=''
	for i in temp :
		ret+=i
	return ret
	

	
for i in range(k):
	current=turn(current)

print(current)


