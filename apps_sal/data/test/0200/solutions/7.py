x=input().split()
y=input().split()
dif=int(x[1])-int(x[0])
cnt=0


if dif-int(y[0])*8<=0:
	print(0)
elif int(y[0])-int(y[1])>0:
	dif=dif-int(y[0])*8+int(y[1])*12
	while dif>0:
		dif-=int(y[0])*12
		if dif<=0:
			cnt+=1
			break
		else :
			cnt+=1
			dif+=int(y[1])*12
	print(cnt)
else: print(-1)
