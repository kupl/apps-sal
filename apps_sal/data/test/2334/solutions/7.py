import math

a = int(input())

b = input().split()
b = [int(i) for i in b]


c = input().split()
c = [int(i) for i in c]

output = 0
for i in b:
	output += (i + c[1] - 1)//(c[0] + c[1])
	
print (output * c[1])
