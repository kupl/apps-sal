stack = []
for i in input().strip():
    if len(stack) == 0:
        stack.append(i)
    elif stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)
if len(stack) == 0:
    print('Yes')
else:
    print('No')
