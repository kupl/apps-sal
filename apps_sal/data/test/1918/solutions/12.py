3

n = int(input())
strength = [int(i) for i in input().split()]
s = input()

total = 0
for i in range(n):
	if s[i] == 'B':
		total += strength[i]
prefix = [0]*n
suffix = [0]*n
for i in range(n):
	if s[i] == 'A':
		if i == 0:
			prefix[i] = 0 + strength[i]
		else:
			prefix[i] = prefix[i-1] + strength[i]
	else:
		if i == 0:
			prefix[i] = 0 - strength[i]
		else:
			prefix[i] = prefix[i-1] - strength[i]

for i in range(n-1, -1, -1):
	if s[i] == 'A':
		if i == n-1:
			suffix[i] = 0 + strength[i]
		else:
			suffix[i] = suffix[i+1] + strength[i]
	else:
		if i == n-1:
			suffix[i] = 0 - strength[i]
		else:
			suffix[i] = suffix[i+1] - strength[i]
x = 0
for i in range(n):
	if prefix[i] > x:
		x = prefix[i]
for i in range(n):
	if suffix[i] > x:
		x = suffix[i]
#print(str(total))
#print(str(x))
total += x
print(str(total))

