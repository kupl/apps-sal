alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def distance(char1,char2):
	x = abs(alphabet.index(char1)-alphabet.index(char2))
	return min(x,26-x)

def changesneeded(s):
	return sum([distance(s[i],'ACTG'[i]) for i in range(4)])

def f(s):
	best = 99999999999
	for i in range(len(s)-3):
		best = min(best,changesneeded(s[i:i+4]))
	return best

n = int(input())
print(f(input()))
