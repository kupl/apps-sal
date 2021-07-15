a=[]

def main():
	n=int(input())
	a.append(0)
	B=input()
	for x in B.split():
		a.append(int(x))
	a.append(0)
	S=sum(a)
	ave=int(S/n)
	ans=0
	for i in range(1,n+1,1):
		if a[i] < ave:
			ans += ave-a[i]
			a[i+1] -= ave-a[i]
		else:
			ans += a[i]-ave
			a[i+1] += a[i]-ave
	print(ans)

main()
