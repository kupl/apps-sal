import math, sys
def main():
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a5 = 0
	a4 = 0
	a3 = 0
	a2 = 0
	a1 = 0
	b5 = 0
	b4 = 0
	b3 = 0
	b2 = 0
	b1 = 0
	ans = 0
	for i in a:
		if i==5:
			a5+=1
		if i==4:
			a4+=1
		if i==3:
			a3+=1
		if i==2:
			a2+=1
		if i==1:
			a1+=1
	for i in b:
		if i==5:
			b5+=1
		if i==4:
			b4+=1
		if i==3:
			b3+=1
		if i==2:
			b2+=1
		if i==1:
			b1+=1
	if (a5+b5)%2==0 and (a4+b4)%2==0 and (a3+b3)%2==0 and (a2+b2)%2==0 and (a1+b1)%2==0:
		ans += max(a5,b5) - (a5+b5)//2
		ans += max(a4,b4) - (a4+b4)//2
		ans += max(a3,b3) - (a3+b3)//2
		ans += max(a2,b2) - (a2+b2)//2
		ans += max(a1,b1) - (a1+b1)//2 
		print(ans//2)
		return
	
	print(-1)
def __starting_point():
	main()

__starting_point()
