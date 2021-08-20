S = input()
stack = []
for s in S:
    if not stack and s != 'B':
        stack.append(s)
    elif s == 'B':
        if stack:
            stack.pop()
        else:
            continue
    else:
        stack.append(s)
print(''.join(stack))
