S = str(input())

stack = []

for s in S:
    if s == '0' or s == '1':
        stack.append(s)
    elif s == 'B':
        if not stack:
            continue
        else:
            stack.pop()

for s in stack:
    print(s, end='')
