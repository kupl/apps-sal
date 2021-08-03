a = input()
b = input()
s = list(input())
for i in range(len(s)):
    e = s[i]
    if 'A' <= e <= 'Z':
        bad = True
        e = chr(ord(e) - ord('A') + ord('a'))
    elif 'a' <= e <= 'z':
        bad = False
    else:
        continue
    e = b[a.index(e)]
    if bad:
        e = chr(ord(e) - ord('a') + ord('A'))
    s[i] = e
print(''.join(s))
