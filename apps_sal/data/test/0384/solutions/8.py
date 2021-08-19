input()
s = input()
l = []
count = 0
for c in range(len(s)):
    if s[c] == 'B':
        count += 1
    elif c and s[c - 1] == 'B':
        l.append(count)
        count = 0
if count:
    l.append(count)
print(len(l))
for i in l:
    print(i)
