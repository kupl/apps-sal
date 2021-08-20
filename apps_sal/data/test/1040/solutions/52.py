n = int(input())
s = input()
l = []
l.append(1)
for i in range(n):
    if l[-1] == 'o':
        if l[-2] == 'f' and s[i] == 'x':
            l.pop()
            l.pop()
        else:
            l.append(s[i])
    else:
        l.append(s[i])
print(len(l) - 1)
