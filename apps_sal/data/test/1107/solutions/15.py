n = int( input() )
s = input()
i=n
l = len(s)
tot = 0
while i<len(s):
	if s[i-1] == s[i-2] == s[i-3]:
	    tot += 1
	i += n
print(tot)

