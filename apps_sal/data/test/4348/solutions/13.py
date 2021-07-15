c = input().split(" ")
a = int(c[0])
b = int(c[1])
inp = input(str())
count = [0 for i in range(26)]
ind = []

for i in range(a):
	count[ord(inp[i])-ord('a')] += 1

running = 0
hit = -1
for i in range(26):
	running += count[i]
	if running >= b:
		hit = i
		break


rem = running - b
counter = 0

for i in range(a-1, -1, -1):
	if ord(inp[i])-ord('a') > hit:
		ind.append(i)
	elif ord(inp[i])-ord('a') == hit and counter < rem:
		counter += 1
		ind.append(i)
	else:
		pass

ind = reversed(ind)

ans = ""

for i in ind:
	ans += inp[i]

print(ans)

