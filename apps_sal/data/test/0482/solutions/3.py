import string

n, k = map(int, input().split())

symbs = []
letters = string.ascii_lowercase[:k]
last = 0
for i in range(n):
	symbs.append(letters[last])
	last+=1
	if last==k:
		last = 0
print(''.join(symbs))
