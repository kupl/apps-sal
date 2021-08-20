s = input()
for (i, x) in enumerate(s):
    if x == 'A':
        break
for (j, x) in enumerate(s[::-1]):
    if x == 'Z':
        break
print(len(s) - i - j)
