class HString:
	def __init__(self, string, base=257, modulo=1000000007):
		self.__base, self.__modulo = base, modulo
		self.__prefix_hash, self.__base_pow, self.__size = [], [1], 0

		self += string
	
	def __add__(self, string):
		for ch in string:
			self.__base_pow.append((self.__base_pow[-1] * self.__base) % self.__modulo)
			if self.__size == 0: self.__prefix_hash.append(ord(ch))
			else: self.__prefix_hash.append((self.__prefix_hash[-1] * self.__base + ord(ch)) % self.__modulo)
			self.__size += 1
		return self
	
	def size(self): return self.__size

	def getModulo(self): return self.__modulo

	def getHashValue(self, st, en):
		value = self.__prefix_hash[en]
		if st > 0:
			value -= ((self.__prefix_hash[st-1] * self.__base_pow[en-st+1]) % self.__modulo)
			if value < 0: value += self.__modulo
		return value

def palindromic_characteristics(s):
	n, org, rev = len(s), HString(s), HString(s[::-1])
	palindrome_level = [[0 for _ in range(n)] for _ in range(n)]
	palindrome_level_count = [0 for _ in range(n + 1)]

	i, j = 0, 0
	while i < n:
		j = i
		while j < n:
			if org.getHashValue(i, j) == rev.getHashValue(n-1-j, n-1-i):
				mid = (i + j) // 2 + (i + j) % 2
				if i > mid-1: palindrome_level[i][j] = 1
				else: palindrome_level[i][j] = palindrome_level[i][mid-1] + 1
				palindrome_level_count[palindrome_level[i][j]] += 1
			j += 1
		i += 1
	
	for i in range(n-1, 0, -1): palindrome_level_count[i] += palindrome_level_count[i+1]
	return palindrome_level_count[1:]

s = input()
print(' '.join(map(str, palindromic_characteristics(s))))
