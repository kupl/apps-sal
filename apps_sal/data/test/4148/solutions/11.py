n = int(input())
s = list(input())
abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(len(s)):
    for j in range(len(abc)):
        if s[i] == abc[j]:
            s[i] = abc[j + n]
            break
print(''.join(s))
