# ANSHUL GAUTAM
# IIIT-D
 



n = int(input())
s = input()
L = []
c = 0
for i in range(len(s)-2):
	if(s[i]=='x' and s[i+1]=='x' and s[i+2]=='x'):
		c += 1
print(c)




















