n = int(input())
s = input()
a = [[s[0]]]
for i in range(1, n):
    if s[i] == s[i - 1]:
        a[-1].append(s[i])
    else:
        a.append([s[i]])
for elem in a:
    if elem[0] in 'aeiouy':
        if len(elem) == 2 and elem[0] in 'eo':
            print(elem[0] * 2, end='')
        else:
            print(elem[0], end='')
    else:
        for i in elem:
            print(i, end='')
