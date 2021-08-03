n = int(input())
s = list(input())
alp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in range(len(s)):
    for j in range(26):
        if s[i] == alp[j]:
            s[i] = alp[j + n]
            break

print(''.join(s))
