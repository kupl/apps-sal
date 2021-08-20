import string
n = int(input())
s = input()
cnt = set()
for i in s.lower():
    cnt.add(i)
cnt = frozenset(cnt)
print(('NO', 'YES')[cnt == frozenset(string.ascii_lowercase)])
