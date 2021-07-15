t=int(input())
for i in range(0,t):
	n=int(input())
	if(n>30):
		if(n!=36 and n!=40 and n!=44):
			print("YES")
			L=[6,10,14,n-30]
			print(*L)
		else:
			if(n==36):
				L=[6,10,15,5]
				print("YES")
				print(*L)
			elif(n==40):
				L=[6,10,15,9]
				print("YES")
				print(*L)
			if(n==44):
				L=[6,10,15,13]
				print("YES")
				print(*L)
	else:
		print("NO")
