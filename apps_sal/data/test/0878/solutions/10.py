import sys
n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(n-1):
	if (l[i+1]==3 and l[i]==2) or (l[i+1]==2 and l[i]==3):
		print ("Infinite")
		return
	else:
		if l[i]==2:
			if l[i+1]==1:
				count+=3
		elif l[i]==1:
			if l[i+1]==2:
				if i>0:
					if l[i-1]==3:
						count+=2
					else:
						count+=3
				else:
					count+=3
			else:
				count+=4
		else:
			if l[i+1]==1:
				count+=4
print ("Finite")
print (count)

