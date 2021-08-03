s = input()
word = []

for i in s:
    if (i not in word):
        word.append(i)
    else:
        print('no')
        return

print('yes')
