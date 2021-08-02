n = int(input())
letters = 'qwertyuiopasdfghjklzxcvbnm'
words = []
for i in range(n):
    words += [input()]

maxL = 0
for i in range(25):
    for j in range(i + 1, 26):
        letter1 = letters[i]
        letter2 = letters[j]
        currentL = 0
        for word in words:
            good = True
            for letter in word:
                if letter != letter1 and letter != letter2:
                    good = False
            if good:
                currentL += len(word)
        if currentL > maxL:
            maxL = currentL
print(maxL)
