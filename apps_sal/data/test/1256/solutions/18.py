s = list(map(str, input().split('+')))
while s.count('') != 0:
    s.remove('')
s.sort()
print('+'.join(s))
