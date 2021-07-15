input()
s = list(input())

def isGlasnaya(char):
    return char in ['a', 'e', 'i', 'o', 'u', 'y']

i = 0
while i + 1 < len(s):
    if isGlasnaya(s[i]) and isGlasnaya(s[i + 1]):
        del s[i + 1]
        i = 0
    else:
        i += 1
print(''.join(s))

