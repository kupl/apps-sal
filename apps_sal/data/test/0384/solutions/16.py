n = int(input())
s = input()
a = []
c = 0
for i in range(len(s)):
    if s[i] == 'B':
        c += 1
    else:
        if c > 0:
            a.append(c)
        c = 0
if c != 0:
    a.append(c)
print(len(a))
for x in a:
    print(x, end=' ')
