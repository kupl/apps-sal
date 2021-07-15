people = int(input())
line = input().split(" ")
line = [int(x) for x in line]
balance = 0
twofive = 0
fifty = 0
hundred = 0
for money in line:
	if money == 25:
		twofive += 1
	elif money == 50:
		if twofive > 0:
			twofive -= 1
			fifty += 1
		else:
			print("NO")
			return
	elif money == 100:
		if fifty > 0 and twofive > 0:
			fifty -= 1
			twofive -= 1
			hundred += 1
		elif twofive > 2:
			twofive -= 3
			hundred += 1
		else:
			print("NO")
			return
print("YES")

