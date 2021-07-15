a=input()
b=a.split()
n=int(b[0])
c=int(b[1])
a=input()
b=a.split()
a=input()
t=a.split()
for i in range(len(b)):
	b[i]=int(b[i])
for i in range(len(t)):
	t[i]=int(t[i])

time=0
coun_lew=0
coun=0
for i in range(n):
	time+=t[i]
	coun=b[i]-c*time
	if coun<=0:
		coun=0
	coun_lew+=coun

time=0
coun_rew=0
coun=0
for i in range(n-1,-1,-1):
	time+=t[i]
	coun=b[i]-c*time
	if coun<=0:
		coun=0
	coun_rew+=coun

if coun_lew>coun_rew:
	print("Limak")
elif coun_lew<coun_rew:
	print("Radewoosh")
else:
	print("Tie")
