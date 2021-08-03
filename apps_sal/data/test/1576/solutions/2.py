s = list(input())
s2 = []
if len(s) % 2 == 0:
    for i in range(len(s)):
        if i % 2 == 0:
            s2.append(s[-1])
            del s[-1]
        else:
            s2.append(s[0])
            del s[0]
else:
    for i in range(len(s)):
        if i % 2 == 1:
            s2.append(s[-1])
            del s[-1]
        else:
            s2.append(s[0])
            del s[0]
s2.reverse()
print(''.join(s2))
