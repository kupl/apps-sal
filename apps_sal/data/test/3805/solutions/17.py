sequence = input().strip()
if len(sequence) % 2 != 0:
    print('No')
else:
    stack = []
    for s in sequence:
        if stack and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    if stack:
        print('No')
    else:
        print('Yes')
