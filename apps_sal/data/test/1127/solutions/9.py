for _ in range(int(input())):
	n=int(input())
	s=input()
	a1=a2=0
	rayz=s[::2]
	bri=s[1::2]
	if n%2:
		if any(int(i)%2 for i in rayz):print(1)
		else:print(2)
	else:
		if any(int(i)%2==0 for i in bri):print(2)
		else:print(1)
