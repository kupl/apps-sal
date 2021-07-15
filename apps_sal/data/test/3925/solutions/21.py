word = input()

maximum = 0
prev = "-"
curlen = 0

for i in word:
	if prev == i:
		maximum = max(maximum, curlen)
		curlen = 1
	else:
		curlen += 1
		prev = i
maximum = max(maximum, curlen)

start = word[0]
left = 1
i = 1
while True:
	if left == len(word):
		break
	if word[i] != start:
		left += 1
		start = word[i]
		i += 1
	else:
		break

start = word[-1]
right = 1
i = len(word) - 2
while True:
	if right == len(word):
		break
	if word[i] != start:
		right += 1
		start = word[i]
		i -= 1
	else:
		break

if len(word) == 1:
	print(1)
else:
	if word[0] != word[-1]:
		poss = left + right
		if poss > len(word):
			print(len(word))
		else:
			print(max(poss, maximum))
	else:
		print(maximum)

