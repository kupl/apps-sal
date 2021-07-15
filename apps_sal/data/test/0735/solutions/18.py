import sys

n = input().split()[0]
n = (int)(n)
alist = input().split()

alist.insert(0,-1)
alist.append(1e9 + 1)
#print (alist)
#print (len(alist))

ans = 1
flag1 = flag2 = -1
n = n + 2
for i in range(n-1):
	if (int)(alist [i]) > (int)(alist [i+1]) :
		flag1 = i
		break
	else :
		continue

#print (flag1)
if flag1 == -1:
	print ("yes\n1 1\n")
	return

for i in range(flag1+1,n-1) :
	if (int)(alist[i]) < (int)(alist [i+1]) :
		flag2 = i
		break
	else :
		continue
#print (flag2)
if flag2 == -1:
	print ("yes\n%d %d\n"%(flag1+1,n-1))
	return

for i in range(flag2+1,n-1):
	if (int)(alist[i]) > (int)(alist[i+1]):
		print("no\n")
		return

#print("here！")

if ((int)(alist[flag2]) < (int)(alist[flag1-1])) or ((int)(alist[flag1]) > (int)(alist[flag2+1])) :
	print("no\n")
	return

print("yes\n%d %d\n"%(flag1,flag2))
