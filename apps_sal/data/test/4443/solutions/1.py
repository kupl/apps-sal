C = input()
word = [chr(i) for i in range(97, 97 + 26)]
count = 0
for i in range(len(word)):
    if C == word[i]:
        count = i
print(word[count + 1])
