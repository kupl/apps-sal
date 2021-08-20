alpha1 = input()
alpha2 = input()
s = input()
n = len(s)
indices = [0 for i in range(26)]
for i in range(26):
    indices[ord(alpha1[i]) - ord('a')] = i
for i in range(n):
    if not s[i].isalpha():
        print(s[i], end='')
    elif ord('A') <= ord(s[i]) and ord(s[i]) <= ord('Z'):
        j = ord(s[i]) - ord('A')
        j = indices[j]
        l = alpha2[j]
        l = chr(ord(l) - ord('a') + ord('A'))
        print(l, end='')
    else:
        j = ord(s[i]) - ord('a')
        j = indices[j]
        l = alpha2[j]
        print(l, end='')
print('')
