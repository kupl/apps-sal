input()
s = input()
all_el = set()
for i in range(len(s)):
    all_el.add(s[i].lower())
if 26 == len(all_el):
    print('YES')
else:
    print('NO')
