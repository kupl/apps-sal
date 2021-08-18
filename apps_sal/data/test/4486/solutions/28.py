s = input()
letters = ''

for i, letter in enumerate(s):
    if i % 2 == 0:
        letters += letter

print(letters)
