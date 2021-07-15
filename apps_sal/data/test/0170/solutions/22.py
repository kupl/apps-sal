x=int(input())
A=list(map(int,input().split()))
A=A[1:]
#print(A)
D=A
#print(D)
B=list(map(int,input().split()))
B=B[1:]
E=B
C=[]
#print(A)
#print(B)
count=0
num=1000
while(num>0):
	if count==999:
		state=10000
		break
	#print(D)
	state=-100
	if A==C:
		state=10
		break
	if B==C:
		state=100
		break
	if A[0]>B[0]:
		A.append(B[0])
		A.append(A[0])
		A=A[1:]
		B=B[1:]
		count=count+1
		#print(A,B)
		state=0
		num=num-1
	if state!=0:	
		if B[0]>A[0]:
			B.append(A[0])
			B.append(B[0])
			B=B[1:]
			A=A[1:]
			count=count+1
			#print(A,B)
			num=num-1
	#if A==D:
	#	if B==E:
	#		state=1000
	#		break
	#if A==E:
	#	if B==D:
	#		state=1000
	#		break
if state==10:
	print(count,2)
if state==100:
	print(count,1)
#CODE BASED ON THE TEST CASES
#MAHESH JASTI
#IIIT HYDERABAD
if state==10000:
	print(-1)

