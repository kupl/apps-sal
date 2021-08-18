input()
s = input()
r = b = 0
op = []
ans = []
for c in s:
    if c == '(':
        if r <= b:
            op.append(False)
            r += 1
            ans.append('0')
        else:
            op.append(True)
            b += 1
            ans.append('1')
    else:
        if op.pop():
            b -= 1
            ans.append('1')
        else:
            r -= 1
            ans.append('0')
print(''.join(ans))
