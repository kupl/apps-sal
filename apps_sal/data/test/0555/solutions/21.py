s = input()
ns = ''
for (i, x) in enumerate(s):
    if '5' <= x <= '8':
        ns += chr(ord('0') + 9 - (ord(x) - ord('0')))
    elif x == '9' and i:
        ns += '0'
    else:
        ns += x
print(ns)
