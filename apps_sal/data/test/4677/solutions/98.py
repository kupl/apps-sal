opperations = list(input())
display_stack = []
for opperation in opperations:
    if opperation == 'B':
        if display_stack:
            display_stack.pop()
    else:
        display_stack.append(opperation)
print(''.join(display_stack))
