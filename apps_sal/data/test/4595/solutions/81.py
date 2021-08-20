s = input()
st = s.find('A')
for i in range(len(s)):
    n = len(s) - i - 1
    t = s[n]
    if t == 'Z':
        en = n
        break
print(en - st + 1)
