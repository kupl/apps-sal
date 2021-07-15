from collections import defaultdict

s = input()
t = input()

dicts = defaultdict(int)
dictt = defaultdict(int)

cs = []
ct = []

for i in range(len(s)):
    dicts[s[i]] += 1
    dictt[t[i]] += 1
    cs.append(dicts[s[i]])
    ct.append(dictt[t[i]])


if cs == ct:
    print('Yes')
else:
    print('No')
