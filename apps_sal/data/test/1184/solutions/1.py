a = input().strip()
s = set()
for i in a:
    if i not in ' {},':
        s.add(i)

print(len(s))
