s = input()
count=0
if int(s[0])%4==0:
	count+=1
for i in range(1,len(s)):
	if int(s[i-1])%2==0 and (s[i] in '048'):
		count+=(i+1)
	elif int(s[i-1])%2==1 and s[i] in '26':
		count+=i
	elif int(s[i])%4==0:
		count+=1
print(count)
