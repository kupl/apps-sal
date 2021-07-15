from collections import Counter
n=int(input())
r=input()
if (n==1):
	print ("Yes")
	return
d=Counter(r)
for i in d:
	if (d[i]>=2):
		print ("Yes")
		return
print ("No")



