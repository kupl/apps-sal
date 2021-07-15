n,m = list(map(int, input().split(" ")))
strings = []
for i in range(n): 
	strings.append(input())

spec = set('#*&')
dig = set('0123456789')
alpha = set('abcdefghijklmnopqrstuvwxyz')


def num(checkset, checkstring):
	m = len(checkstring)+1
	for i, c in enumerate(checkstring):
		if c in checkset:
			m = min(m, i)
			m = min(m, len(checkstring)-i)
	if m < len(checkstring)+1:
		return m
	return -1 
	
ret = float('inf')
	
for i in range(n):
	for j in range(n):
		for k in range(n):
			if i==j or i==k or j==k:
				continue
			else:
				s1 = num(spec, strings[i])
				s2 = num(dig, strings[j])
				s3 = num(alpha, strings[k]) 
				if s1 >= 0 and s2 >= 0 and s3 >= 0:
					ret = min(ret, s1+s2+s3)

print(str(int(ret)))

					 
				

