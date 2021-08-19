s = input()
a = s.count('a')
l2 = (len(s) - a) // 2
l1 = len(s) - l2
if s[:l1].replace('a', '') == s[l1:]:
    print(s[:l1])
else:
    print(':(')
