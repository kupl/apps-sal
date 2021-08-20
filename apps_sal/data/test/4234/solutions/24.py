n = int(input())
s = list(input())
i = 0
j = 1
while j < len(s):
    while j < len(s) and s[i] == s[j]:
        s[j] = ''
        j += 1
    i = j + 1
    j += 2
if (len(s) - s.count('')) % 2 == 1:
    i = n - 1
    while i >= 0 and s[i] == '':
        i -= 1
    s[i] = ''
print(s.count(''))
print(''.join(s))
