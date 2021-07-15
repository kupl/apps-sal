def main(n,m,c,t,moments):
	s = 0
	answer = []
	last = 0

	for i in range(n):
		s += c[i]*t[i]
		while last<m:
			item = moments[last]
			if item<=s:
				answer.append(i+1)
			else:
				break
			last+=1
		if last>=m:
			break

	s = ''
	for a in answer:
		s+=str(a)+'\n'
	return s[:-1]

def init():
	n,m = list(map(int, input().split()))
	c = []
	t = []

	for i in range(n):
		q,w = list(map(int, input().split()))
		c.append(q)
		t.append(w)

	moments = list(map(int, input().split()))

	print(main(n,m,c,t,moments))

init()
