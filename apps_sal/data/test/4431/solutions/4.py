import sys

n, k = map(int, sys.stdin.readline().strip().split(' '))
s = sys.stdin.readline().strip()
letters = sys.stdin.readline().strip().split(' ')

#print(n, k, s, letters)
#print(len(s))

current_counter = 0
result = 0
for c in s:
	if c in letters:
		current_counter += 1
	else:
		result += current_counter * (current_counter + 1) // 2
		current_counter = 0

result += current_counter * (current_counter + 1) // 2
print(result)
