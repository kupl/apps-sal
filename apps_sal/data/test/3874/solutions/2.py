import sys
import re

[words, selected] = input().split(" ")
[words, selected] = [int(words), int(selected)]
wordBuffer = []
selectedWords = []

for i in range(words):
    wordBuffer.append(input())
buffer = input().split(" ")
for i in buffer:
    selectedWords.append(wordBuffer[int(i) - 1])

for i in range(len(selectedWords)):
    if (i > 0 and len(selectedWords[i - 1]) != len(selectedWords[i])):
        print("No")
        return

reg = ""
res = ""
for letter in range(len(selectedWords[0])):
    isQuested = False
    for i in range(selected):
        if (i > 0 and selectedWords[i - 1][letter] != selectedWords[i][letter]):
            reg += "."
            res += "?"
            isQuested = True
            break
    if (isQuested == False):
        if (selectedWords[0][letter] == "."):
            reg += "\\" + selectedWords[0][letter]
        else:
            reg += selectedWords[0][letter]
        res += selectedWords[0][letter]

matches = 0
for i in wordBuffer:
    if (re.fullmatch(reg, i) != None):
        matches += 1

if (matches == selected):
    print("Yes\n" + res)
else:
    print("No")

