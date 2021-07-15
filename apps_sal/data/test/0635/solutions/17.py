n,s=list(map(int, input().split()))
a=list(map(int, input().split()))
b=list(map(int, input().split()))
if a[0] != 1:
	print("NO")
elif [0]*n == a:
	print("NO")
else:
	if a[s-1] == 1:
		print("YES")
	else:
		if b[s-1] == 0:
			print("NO")
		else:
			flag=0
			for i in range(s,n):
				if a[i]==1 and b[i]==1:
					print("YES")
					flag=1
					break
			if flag==0:
				print("NO")
				

