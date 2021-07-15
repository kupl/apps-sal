import sys
s = input()
z = True
for i in range(len(s)):
    if not z:
        break
    try:
        if s[i] == s[i + 1]:
            print((i + 1, i + 2))
            z = False
            return
        if s[i] == s[i + 2]:
            print((i + 1, i + 3))
            z = False
            return
    except:
        pass
if z:
    print((-1, -1))

