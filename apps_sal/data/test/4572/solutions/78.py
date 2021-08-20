alphabets = [chr(ord('a') + i) for i in range(26)]
for a in list(input()):
    if a in alphabets:
        alphabets.remove(a)
if alphabets:
    print(alphabets[0])
else:
    print('None')
