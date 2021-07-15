n = int(input())
a = list(map(int, input().split()))
l = 0
r = n - 1
ot = []
prot = ""
if a[l] < a[r]:
	ot.append(a[l])
	l += 1
	prot += "L"
else:
	ot.append(a[r])
	r -= 1
	prot += "R"
run = True
while run:
	if l > r:
		#print("A")
		run = False
	elif l == r:
		if a[l] >= ot[-1]:
			prot += "R"
		#print("B")
		run = False
	else:
		if ot[-1] <= a[l] <= a[r]:
			ot.append(a[l])
			l += 1
			prot += "L"
			#print("1")
		elif ot[-1] <= a[r] <= a[l]:
			ot.append(a[r])
			r -= 1
			prot += "R"
			#print("2")
		elif ot[-1] <= a[l]:
			ot.append(a[l])
			l += 1
			prot += "L"
			#print("3")
		elif ot[-1] <= a[r]:
			ot.append(a[r])
			r -= 1
			prot += "R"
			#print("4")
		else:
			#print("C")
			run = False
print(len(prot))
print(prot)

