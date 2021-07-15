n=int(input())
l=list(map(int, input().split()))
l.sort()
final=[]
for i in l:
	if i not in final:
		final+=[i]
if(len(final)==1):
	print(0)
elif(len(final)==2):
	if((final[1]-final[0])%2==0):
		print((final[1]-final[0])//2)
	else:
		print(final[1]-final[0])
elif(len(final)==3):
	if((final[1]-final[0])==(final[2]-final[1])):
		print(final[2]-final[1])
	else:
		print(-1)
else:
	print(-1)
