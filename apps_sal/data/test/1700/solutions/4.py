n = int(input())
A = input()

stack = []

for i in A:
    if i == '(':
        if len(stack) == 0 or stack[-1] == 1:
            stack.append(0)
            print(0, end='')
        else:
            stack.append(1)
            print(1, end='')
    else:
        print(stack[-1], end='')
        stack.pop()
