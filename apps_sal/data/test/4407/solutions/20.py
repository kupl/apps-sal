def main():
	d={}
	nums=[None]*31
	for i in range(31):
		nums[i]=2**i
		d[nums[i]]=0

	n,q=map(int,input().split())
	a=list(map(int,input().split()))
	for i in range(n):
		d[a[i]]+=1
	for i in range(31):
		if d[nums[i]]==0:
			del d[nums[i]]
	keys=sorted(list(d.keys()))[::-1]
	leng=len(keys)
	ans=[0]*q
	for i in range(q):
		val=int(input())
		for j in range(leng):
			if keys[j]<=val:
				coin=min(d[keys[j]],val//keys[j])
				ans[i]+=coin
				val-=keys[j]*coin
				if val==0:
					break
		else:
			ans[i]=-1

	print('\n'.join(list(map(str,ans))))

main()
