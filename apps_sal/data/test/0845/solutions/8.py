letters = list('qwertyuiopasdfghjkl;zxcvbnm,./')
output = ''
i = 1 if input() == 'L' else -1
for c in input():
	output += letters[letters.index(c) + i]
print(output)

