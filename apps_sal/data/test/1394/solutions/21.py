def astrip(s):
	return ''.join([char for char in s if char != 'a'])

def f(s):
	t = astrip(s)
	n = len(t)
	if n % 2 != 0:
		return ':('
	k = n // 2
	candidate = t[:-1*k]
	if t != candidate + candidate:
		return ':('
	if s[len(s)-k:] == candidate:
		return s[:len(s)-k]
	return ':('

print(f(input()))
