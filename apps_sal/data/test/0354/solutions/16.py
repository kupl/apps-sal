import sys

s = input()
t = input()

if len(s) != len(t):
    print('No')
    return

VOWELS = 'aeiou'

for a, b in zip(s, t):
    if a in VOWELS and b not in VOWELS or b in VOWELS and a not in VOWELS:
        print('No')
        return

print('Yes')

