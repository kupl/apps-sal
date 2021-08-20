from sys import stdin, stdout
import string
n = int(stdin.readline().rstrip())
s = list(stdin.readline().rstrip())
lset = str(string.ascii_lowercase)
uset = str(string.ascii_uppercase)
currentSet = set()
maxSize = 0
for letter in s:
    if letter in uset:
        currentSet = set()
    else:
        currentSet.add(letter)
        maxSize = max(maxSize, len(currentSet))
print(maxSize)
