from collections import Counter
s = input()
c = Counter(s)
l = (len(s) + c['a']) // 2
if s[:l].replace('a', '') == s[l:]:
    print(s[:l])
else:
    print(':(')
