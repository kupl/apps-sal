s = input()
first_index = s.index('A', 0)
last_index = 0
for i in range(1, len(s)):
    if s[-i] == 'Z':
        last_index = len(s) - i
        break
print(last_index - first_index + 1)
