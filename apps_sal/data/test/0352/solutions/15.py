n=int(input())
min1,max1=map(int,input().split())
min2,max2=map(int,input().split())
min3,max3=map(int,input().split())
if max1+max2+max3==n:
	print(str(max1),str(max2),str(max3))
	quit()
if max1+max2+min3<=n:
	print(str(max1),str(max2),str(n-max1-max2))
	quit()
if max1+min2+min3<=n:
	print(str(max1),str(n-max1-min3),str(min3))
	quit()
print(str(n-min2-min3),str(min2),str(min3))
