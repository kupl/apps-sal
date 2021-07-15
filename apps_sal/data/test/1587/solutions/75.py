N = int(input())
c = input()
c = list(c)
t = True

i = 0
j = N - 1
count = 0

while t:
	if c[i] == "R":
		i += 1
	elif c[j] == "W":
		j -= 1
	elif c[i] == "W" and c[j] == "R":
		c[i] = "R"
		c[j] = "W"
		count += 1	
	if i >= j:
		t = False
		break
print(count)

