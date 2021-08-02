s = input()
alc = 0
for c in s:
    if c != '0':
        if c == '1':
            alc += 10
        elif '1' < c <= '9':
            alc += ord(c) - ord('0')
        else:
            alc += (lambda x: {'J': 11, 'Q': 12, 'K': 13, 'A': 1}[x])(c)
print(alc)
