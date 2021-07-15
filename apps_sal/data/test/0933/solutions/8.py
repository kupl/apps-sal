__author__ = 'Lipen'

def actions(s):
	if len(s)<=2:
		return s

	lasttwo = s[0],s[1]
	formated = s[0:2]

	for c in s[2:]:
		if not (c==lasttwo[0] and c==lasttwo[1]):
			formated += c
			lasttwo = lasttwo[1], c

	if len(formated)<=3:
		return formated
	lastthree = formated[0], formated[1], formated[2]

	answer = formated[0:3]

	for i in range(3,len(formated)):
		c = formated[i]
		if not (lastthree[0]==lastthree[1] and lastthree[2]==c):
			answer += c
			lastthree = lastthree[1], lastthree[2], c

	return answer

def main():
	s = input()

	print(actions(s))

def __starting_point(): main()
__starting_point()
