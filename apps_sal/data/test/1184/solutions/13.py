s = input()
if s == '{}':
    c = set()
else:
    c = set(s[1:len(s) - 1].split(', '))
print(len(c))
