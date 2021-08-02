n = int(input())
s = input()
stack = []
for c in s:
    if stack == []: stack.append(c)
    elif stack[len(stack) - 1] + c == '10' or stack[len(stack) - 1] + c == '01': stack.pop(len(stack) - 1)
    else: stack.append(c)
print(len(stack))
