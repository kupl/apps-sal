from math import ceil, log
t = 1
for test in range(t):
	n = int(input())
	openB=[0 for i in range(300001)]
	closeB=[0 for i in range(300001)]
	ans = 0
	zero = 0
	for i in range(n):
		string = input()
		arr = [0]
		plus = 0
		minus = 0
		for char in string:
			if char == "(":
				plus+=1
				arr.append(1)
			else:
				if arr[-1]==1:
					plus-=1
					arr.pop()
				else:
					minus +=1
		if plus and minus:
			continue
		elif plus:
			openB[plus]+=1
		elif minus:
			closeB[minus]+=1
		else:
			zero += 1
	for i in range(300001):
		ans+=openB[i]*closeB[i]
	print(ans+(zero*zero))




	


