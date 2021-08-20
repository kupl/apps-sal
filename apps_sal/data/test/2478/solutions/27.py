N = int(input())
S = input()
stack = []
for c in S:
    if len(stack) > 0:
        last = stack[-1]
        if last == '(' and c == ')':
            stack = stack[:-1]
            continue
    stack.append(c)
left = stack.count(')')
right = stack.count('(')
print(left * '(' + S + right * ')')
