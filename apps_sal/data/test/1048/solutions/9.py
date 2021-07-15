n = int(input())
s = input()
x = [0 for i in range(4)]
for i in range(n):
	if s[i] == "U":
		x[0] += 1
	elif s[i] == "D":
		x[1] += 1
	elif s[i] == "L":
		x[2] += 1
	else:
		x[3] += 1
print(min(x[0], x[1]) * 2 + min(x[2], x[3]) * 2)		
		
		

