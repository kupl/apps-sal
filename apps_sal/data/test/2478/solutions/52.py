n = int(input())
s = str(input())
l = []
(left, right) = (0, 0)
for c in s:
    if c == ')':
        if l == []:
            left += 1
        else:
            l.pop()
    else:
        l.append(1)
right = len(l)
print('(' * left + s + ')' * right)
