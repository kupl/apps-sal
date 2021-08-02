s = input()
sta = []
fin = []
for i in range(len(s)):
    if s[i] == 'A':
        sta.append(i)
    elif s[i] == 'Z':
        fin.append(i)
print(max(fin) - min(sta) + 1)
