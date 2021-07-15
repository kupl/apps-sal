s=input()
ab=0
ba=0
aba=0
bab=0
n=len(s)
if n<4:
	print("NO")
else:
	for i in range(n-1):
		if s[i:i+2]=="AB":ab+=1
	for i in range(n-1):
		if s[i:i+2]=="BA":ba+=1
	for i in range(n-2):
		if s[i:i+3]=="ABA":aba+=1
	for i in range(n-2):
		if s[i:i+3]=="BAB":bab+=1
	if ab==0 or ba==0:
		print("NO")
	elif ab==1 and ba==1:
		if bab==1 or aba==1:
			print("NO")
		else:
			print("YES")
	elif ab==1 and ba==2:
		if bab==1 and aba==1:print("NO")
		else:print("YES")
	elif ab==2 and ba==1:
		if bab==1 and aba==1:print("NO")
		else:print("YES")
	else:print("YES")
