# import math
# import statistics
#a=input()
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#    c.append(i)
e1,e2 = list(map(str,input().split()))
#K = input()
# f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
count=0
a=e1+e2
for i in range(1,int(a)):
	if int(a)/int(i)==int(i):
		count+=1
if count>0:
	print('Yes')
else:
	print('No')

