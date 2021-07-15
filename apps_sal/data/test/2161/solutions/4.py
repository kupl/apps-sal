def print_arr(arr):
	for i in arr:
		print(i, "", end="")
	print()	


n = int(input())
d = {}
for _ in range(n):
	name, num, *numbers = input().split()
	if name in d:
		s = d[name]
	else:
		s = []	
	for nm in numbers:
		for i in s:
			if i.endswith(nm):
				state=1
				break
			if nm.endswith(i):
				s.remove(i)
		else:
			s.append(nm)
	d[name] = s
	
print(len(d))	
for name in d:
	print(name, len(d[name]), end=" ")
	print_arr(d[name])							
