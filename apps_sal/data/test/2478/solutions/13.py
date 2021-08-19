n = int(input())
s = input()
l = []
for i in s:
    if i == ')':
        if len(l) > 0:
            if l[-1] == '(':
                l.pop()
            else:
                l.append(i)
        else:
            l.append(i)
    else:
        l.append(i)
print(l.count(')') * '(' + s + l.count('(') * ')')
