n = int(input())
s = input()
ind = True
ind1 = False
y = []
for i in s:
	y.append(i)
for i in range(n):
	if (y[i] == "?" and i == 0) or (y[i] == "?" and i == n - 1) or (y[i] == "?" and y[i - 1] == y[i + 1]) or (y[i] == "?" and (y[i - 1] == "?" or y[i + 1])) == "?":
		ind1 = True
	if i > 0 and (y[i] == y[i - 1] and y[i] != "?"):
		ind = False
		break
if ind and ind1:
	print("Yes")
else:
	print("No")	

