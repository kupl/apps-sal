n = int(input())
s = str(input())
stack = []
for c in s:
    if c == 'x':
        if len(stack) < 2:
            stack.append(c)
        elif stack[-2] == 'f' and stack[-1] == 'o':
            stack.pop()
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)
print(len(stack))
