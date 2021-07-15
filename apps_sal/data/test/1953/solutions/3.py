n=input()
inp=[int(x) for x in input().split()]
inp.sort()
count=0
time=0
for i in inp:
	if time<=i:
		time+=i
		count+=1
print(count)

