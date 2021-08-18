
stack = ['
for c in input():
    if stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)

stack.pop()
print("No" if len(stack) else "Yes")
