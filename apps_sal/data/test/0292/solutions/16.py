h, n = (int(x) for x in input().split())
leftPlus, rightPlus = 1, 2**h
answer = 1
curLevel = 0
delim = 2**(h - 1)
while curLevel != h:
	h -= 1
	if n <= delim:
		answer += leftPlus
		leftPlus, rightPlus = max(rightPlus // 2, leftPlus // 2), 1
		delim -= 2**(h - 1)
		# print ("L", answer)
	else:
		answer += rightPlus
		leftPlus, rightPlus = 1, max(rightPlus // 2, leftPlus // 2)
		delim += 2**(h - 1)
		# print ("R", answer)	
print (answer - 1)
