s = input()
v = 0
cons = 0
consonant = []
n = len(s)
vowels = ['A', 'E', 'I', 'O', 'U']
if(n < 8):
    print(-1)
    return
for i in range(n):
    if(s[i] in vowels and v == 0):
        if(s[i + 1] in vowels and s[i + 2] in vowels):
            v = 1
    if(s[i] not in vowels and s[i] not in consonant):
        cons += 1
        consonant.append(s[i])
if(v == 1 and cons >= 5):
    print("GOOD")
else:
    print(-1)
