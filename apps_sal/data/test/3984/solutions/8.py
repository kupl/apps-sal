s = input()
l = len(s)
d = [s[0] for i in range(l)]
print('Mike')
for i in range(1, l):
    d[i] = min(d[i - 1], s[i])
    if d[i] < s[i]:
        print('Ann')
    else:
        print('Mike')
