input()
s = list(input())
found = True

while found:
    x = []
    found = False
    i = 0
    while i < len(s) - 1:
        ss = [s[i], s[i + 1]]
        if 'R' in ss and 'U' in ss:
            x.append('D')
            i += 2
            found = True
        else:
            x.append(s[i])
            i += 1
    if i < len(s):
        x.append(s[i])
    s = x

print(len(s))
