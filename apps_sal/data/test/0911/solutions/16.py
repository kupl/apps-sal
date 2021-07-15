n,c=list(map(int,input().split()))
in1=list(map(int,input().split()))
in2=list(map(int,input().split()))
t1,t2,op1,op2=0,0,0,0
for i in range(0,n):
	t1+=in2[i]
	op1+=(in1[i]-c*t1 if(in1[i]-c*t1)>0 else 0)
	t2+=in2[n-i-1]
	op2+=(in1[n-i-1]-c*t2 if(in1[n-i-1]-c*t2)>0 else 0)
if(op1==op2):
	print("Tie")
else:
	print("Limak" if op1>op2 else "Radewoosh")

