n = int(input())
s = input()
ar = []
gl = ['a', 'e', 'i', 'o', 'u', 'y']
i = 0
while i < len(s):
    it = False
    if (s[i] in gl):
        it = True
    if (it):
        cnt = 0
        c = s[i]
        j = i
        while (j < len(s) and s[j] == s[i]):
            cnt += 1
            j += 1

        if ((s[i] == 'e' or s[i] == 'o') and j - i == 2):
            ar.append(s[i])
            ar.append(s[i])

        else:
            ar.append(s[i])
        i = j
    else:
        ar.append(s[i])
        i += 1
print(''.join(ar))
