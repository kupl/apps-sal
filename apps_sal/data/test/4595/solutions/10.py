s = input()
a = len(s)
z = 0
for (i, e) in enumerate(reversed(s)):
    if e == 'A':
        a = len(s) - i - 1
for (i, e) in enumerate(s):
    if e == 'Z':
        z = i
print(z - a + 1)
