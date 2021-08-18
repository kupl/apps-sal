n = int(input())
si = input()
s = []
for i in si:
    s.append(i)

dic = {0: 'R', 1: 'G', 2: 'B'}
dic2 = {'R': 0, 'G': 1, 'B': 2}
c = 0
for i in range(1, len(s)):
    if i == (len(s) - 1):
        if s[i] == s[i - 1]:
            s[i] = dic[(dic2[s[i]] + 1) % 3]
            c += 1
    else:
        if s[i] == s[i - 1]:
            if s[i + 1] == s[i - 1]:
                s[i] = dic[(dic2[s[i]] + 1) % 3]
                c += 1
            else:
                temp = [False] * 3
                temp[dic2[s[i - 1]]] = True
                temp[dic2[s[i + 1]]] = True
                for j in range(3):
                    if not temp[j]:
                        s[i] = dic[j]
                        c += 1
print(c)
for i in s:
    print(i, end='')
