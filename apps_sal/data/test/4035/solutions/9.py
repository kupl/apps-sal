A,B=map(int,input().split())
for i in range(1500):
	if(i*2//25==A)*(i//10==B):print(i);return
print(-1)
