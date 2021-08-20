s = input()
first_index = s.index('A', 0)
last_index = 0
for (i, ss) in enumerate(s):
    if ss == 'Z':
        last_index = i
print(last_index - first_index + 1)
