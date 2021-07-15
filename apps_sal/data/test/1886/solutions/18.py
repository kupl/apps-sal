word = input()
if (len(word) > 1):
    print("%s%s" % (word[0].upper(), word[1:]))
else:
    print(word.upper())

