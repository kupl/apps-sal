s = input()
if '[' in s and ']' in s:
    a = s.index('[') + 1
    b = len(s)-s[::-1].index(']') - 1
else:
    print(-1)
    return
s = s[a:b]
if s.count(':') >= 2:
    a = s.index(':')+1
    b = len(s)-s[::-1].index(':')-1
else:
    print(-1)
    return
c = 0
for el in s[a:b]:
    if el =='|':
        c += 1
print(4 + c)
