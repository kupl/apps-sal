3

c = 26*[0]
ind = 26*[0]
for i in range(26):
	c[i] = chr(i+97)
	ind[i] = i
n,m = map(int, input().split())
s = input()
size = len(s)
s1 = size*[0]
for _ in range(m):
	x,y = input().split()
	c[ind[ord(x)-97]] = y
	c[ind[ord(y)-97]] = x
	ind[ord(x)-97],ind[ord(y)-97] = ind[ord(y)-97],ind[ord(x)-97]
for i in range(size):
	s1[i] = c[ord(s[i])-97]
print (('').join(s1))
