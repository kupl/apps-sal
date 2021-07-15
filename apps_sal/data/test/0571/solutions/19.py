import sys

def main():
	n = int(input())
	
	s = list(sys.stdin.readline())
	f, ouv = 0, 0
	
	for i in range(n):
		if s[i] == '?' or s[i] == '(':
			ouv += 1
		else:
			f +=1
			ouv -= 1
		#print(i, f, ouv, file = sys.stderr)
		if i < n-1 and ouv <= 0:
			print(':(')
			return

	f, ouv = 0, 0

	for i in range(n):
		if s[n-1-i] == '?' or s[n-1-i] == ')':
			f += 1
		else:
			ouv +=1
			f -= 1
		#print(n-1-i, f, ouv, file = sys.stderr)
		if i < n-1 and f <= 0:
			print(':(')
			return

	if n%2 == 1:
		print(':(')
		return

	k = n//2 - ouv

	for i in range(n):
		if s[i] == '?' and k != 0:
			s[i] = '('
			k-=1
		elif s[i] == '?':
			s[i] = ')'

	print(*s, sep='')

main()
