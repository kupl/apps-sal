''' author: Priyank Koul, PES University, Bengaluru'''
for _ in range(int(input())):
	x= int(input())
	li= list(map(int, input().strip().split()))
	fli=[]
	for i in range(1,x):
		fli.append(li[i]-li[i-1])
	if(sum(fli)<0):
		print("NO")
	else:
		print("YES")
		
		
		
		

