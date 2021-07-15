n = int(input())
s = input()
vowel = "aeiouy"
first = 0
for x in s:
	if x in vowel and not first:
		first = 1
		print(x, end="")
	elif x not in vowel:
		first = 0
		print(x, end="")
print()

