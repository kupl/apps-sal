# cook your dish here
A,B,C=map(int,input().split())
if ((C-A)//B)%2==0:
	print("Lucky Chef")
else:
	print("Unlucky Chef")
