n, m = input().split()
n, m = int(n), int(m)

a = input().split()
b = input().split()

a = [int(k) for k in a]
b = [int(k) for k in b]

s1 = [a[0]]
s2 = [b[0]]

for i in range(1,len(a)):
	s1.append(s1[i-1]+a[i])

for i in range(1,len(b)):
	s2.append(s2[i-1]+b[i])

#print(s1)
#print(s2)

i1=0
i2=0
count=0

while i1<len(s1) or i2<len(s2):
	#print(i1, i2)
	if (s1[i1]==s2[i2]):
		count+=1
		i1+=1
		i2+=1
	elif (s1[i1]<s2[i2]):
		i1+=1
	elif (s1[i1]>s2[i2]):
		i2+=1

print(count)
