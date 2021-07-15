def palindromic_characteristics(s):
	n = len(s)
	palindrome_level = [[0 for _ in range(n)] for _ in range(n)]
	palindrome_level_count = [0 for _ in range(n + 1)]

	for i in range(n):
		j = i
		while i >= 0 and j < n and s[i] == s[j]:
			palindrome_level[i][j] = 1
			i, j = i - 1, j + 1
	
	for i in range(n-1):
		j = i + 1
		while i >= 0 and j < n and s[i] == s[j]:
			palindrome_level[i][j] = 1
			i, j = i - 1, j + 1

	for i in range(n):
		for j in range(i, n):
			if palindrome_level[i][j] > 0:
				mid = (i + j) // 2 + (i + j) % 2
				if i <= mid-1: palindrome_level[i][j] = palindrome_level[i][mid-1] + 1

				palindrome_level_count[palindrome_level[i][j]] += 1
	
	for i in range(n-1, 0, -1): palindrome_level_count[i] += palindrome_level_count[i+1]
	return palindrome_level_count[1:]

s = input()
print(' '.join(map(str, palindromic_characteristics(s))))
