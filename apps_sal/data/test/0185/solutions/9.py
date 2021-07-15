n,k=list(map(int,input().split()))
diff1=k-1
diff2=n-k
ans=2
if(diff1<=diff2):
	ans+=4*(diff1)
	ans+=1
	ans+=3*(diff2)
else:
	ans+=4*(diff2)
	ans+=1
	ans+=3*(diff1)
print(ans)

