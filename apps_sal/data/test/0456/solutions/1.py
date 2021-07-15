n = int(input())
s = input().strip()

rez = ''
i = 0
while i < len(s):
	if s[i:i + 3] == 'ogo':
		j = i + 3
		while s[j:j + 2] == 'go':
			j += 2
		i = j
		rez += '***'
	else:
		rez += s[i]
		i += 1

print(rez)
