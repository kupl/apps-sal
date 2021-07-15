actual_vals = [0 for x in range(4)]
required_vals = [1 for x in range(4)]
l1,s1,r1,p1 = list(map(int,input().split()))
if(l1==1):
	required_vals[3] = 0
if(s1==1):
	required_vals[2] = 0
if(r1==1):
	required_vals[1] = 0
if(l1==1 or r1==1 or s1==1):
	required_vals[0] = 0
actual_vals[0] = p1

l2,s2,r2,p2 = list(map(int,input().split()))
if(l2==1):
	required_vals[0] = 0
if(s2==1):
	required_vals[3] = 0
if(r2==1):
	required_vals[2] = 0
if(l2==1 or r2==1 or s2==1):
	required_vals[1] = 0
actual_vals[1] = p2

l3,s3,r3,p3 = list(map(int,input().split()))
if(l3==1):
	required_vals[1] = 0
if(s3==1):
	required_vals[0] = 0
if(r3==1):
	required_vals[3] = 0
if(l3==1 or r3==1 or s3==1):
	required_vals[2] = 0
actual_vals[2] = p3

l4,s4,r4,p4 = list(map(int,input().split()))
if(l4==1):
	required_vals[2] = 0
if(s4==1):
	required_vals[1] = 0
if(r4==1):
	required_vals[0] = 0
if(l4==1 or r4==1 or s4==1):
	required_vals[3] = 0
actual_vals[3] = p4

for i in range(4):
	if(required_vals[i]==0 and actual_vals[i]==1):
		print('YES')
		return
print('NO')

