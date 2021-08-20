__author__ = 'Think'
name = input()
prev = 'a'
total = 0
for s in name:
    total += min(abs(ord(s) - ord(prev)), 26 - abs(ord(s) - ord(prev)))
    prev = s
print(total)
