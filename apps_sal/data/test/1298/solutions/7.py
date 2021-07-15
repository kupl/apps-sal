__author__ = 'Andrey'
n = int(input())
num = input()
stack = []
for char in num:
    if len(stack) == 0:
        stack.append(char)
    elif char != stack[-1]:
        stack.pop()
    else:
        stack.append(char)
print(len(stack))
