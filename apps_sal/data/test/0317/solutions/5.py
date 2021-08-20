nums = int(input())
the_str = str(input()).lower()
d = set()
for ch in the_str:
    if ch >= 'a' and ch <= 'z':
        d.add(ch)
if len(d) == 26:
    print('YES')
else:
    print('NO')
