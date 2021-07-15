import sys

p=[int(x) for x in input().split('+')]
p.sort()
for i in range(len(p)-1):
	sys.stdout.write(str(p[i]))
	sys.stdout.write('+')
print(str(p[len(p)-1]))


